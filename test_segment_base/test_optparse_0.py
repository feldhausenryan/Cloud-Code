"""
        self.file_help = "read from FILE [default: %default]"
        self.expected_help_file = self.help_prefix + \
            "  -f FILE, --file=FILE  read from FILE [default: foo.txt]\n"
        self.expected_help_none = self.help_prefix + \
            "  -f FILE, --file=FILE  read from FILE [default: none]\n"

    def test_option_default(self):
        self.parser.add_option("-f", "--file",
                               default="foo.txt",
                               help=self.file_help)
        self.assertHelp(self.parser, self.expected_help_file)

    def test_parser_default_1(self):
        self.parser.add_option("-f", "--file",
                               help=self.file_help)
        self.parser.set_default('file', "foo.txt")
        self.assertHelp(self.parser, self.expected_help_file)

    def test_parser_default_2(self):
        self.parser.add_option("-f", "--file",
                               help=self.file_help)
        self.parser.set_defaults(file="foo.txt")
        self.assertHelp(self.parser, self.expected_help_file)

    def test_no_default(self):
        self.parser.add_option("-f", "--file",
                               help=self.file_help)
        self.assertHelp(self.parser, self.expected_help_none)

    def test_default_none_1(self):
        self.parser.add_option("-f", "--file",
                               default=None,
                               help=self.file_help)
        self.assertHelp(self.parser, self.expected_help_none)

    def test_default_none_2(self):
        self.parser.add_option("-f", "--file",
                               help=self.file_help)
        self.parser.set_defaults(file=None)
        self.assertHelp(self.parser, self.expected_help_none)

    def test_float_default(self):
        self.parser.add_option(
            "-p", "--prob",
            help="blow up with probability PROB [default: %default]")
        self.parser.set_defaults(prob=0.43)
        expected_help = self.help_prefix + \
            "  -p PROB, --prob=PROB  blow up with probability PROB [default: 0.43]\n"
        self.assertHelp(self.parser, expected_help)

    def test_alt_expand(self):
        self.parser.add_option("-f", "--file",
                               default="foo.txt",
                               help="read from FILE [default: *DEFAULT*]")
        self.parser.formatter.default_tag = "*DEFAULT*"
        self.assertHelp(self.parser, self.expected_help_file)

    def test_no_expand(self):
        self.parser.add_option("-f", "--file",
                               default="foo.txt",
                               help="read from %default file")
        self.parser.formatter.default_tag = None
        expected_help = self.help_prefix + \
            "  -f FILE, --file=FILE  read from %default file\n"
        self.assertHelp(self.parser, expected_help)


# -- Test parser.parse_args() ------------------------------------------

class TestStandard(BaseTest):
    def setUp(self):
        options = [make_option("-a", type="string"),
                   make_option("-b", "--boo", type="int", dest='boo'),
                   make_option("--foo", action="append")]

        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE,
                                               option_list=options)

    def test_required_value(self):
        self.assertParseFail(["-a"], "-a option requires an argument")

    def test_invalid_integer(self):
        self.assertParseFail(["-b", "5x"],
                             "option -b: invalid integer value: '5x'")

    def test_no_such_option(self):
        self.assertParseFail(["--boo13"], "no such option: --boo13")

    def test_long_invalid_integer(self):
        self.assertParseFail(["--boo=x5"],
                             "option --boo: invalid integer value: 'x5'")

    def test_empty(self):
        self.assertParseOK([], {'a': None, 'boo': None, 'foo': None}, [])

    def test_shortopt_empty_longopt_append(self):
        self.assertParseOK(["-a", "", "--foo=blah", "--foo="],
                           {'a': "", 'boo': None, 'foo': ["blah", ""]},
                           [])

    def test_long_option_append(self):
        self.assertParseOK(["--foo", "bar", "--foo", "", "--foo=x"],
                           {'a': None,
                            'boo': None,
                            'foo': ["bar", "", "x"]},
                           [])

    def test_option_argument_joined(self):
        self.assertParseOK(["-abc"],
                           {'a': "bc", 'boo': None, 'foo': None},
                           [])

    def test_option_argument_split(self):
        self.assertParseOK(["-a", "34"],
                           {'a': "34", 'boo': None, 'foo': None},
                           [])

    def test_option_argument_joined_integer(self):
        self.assertParseOK(["-b34"],
                           {'a': None, 'boo': 34, 'foo': None},
                           [])

    def test_option_argument_split_negative_integer(self):
        self.assertParseOK(["-b", "-5"],
                           {'a': None, 'boo': -5, 'foo': None},
                           [])

    def test_long_option_argument_joined(self):
        self.assertParseOK(["--boo=13"],
                           {'a': None, 'boo': 13, 'foo': None},
                           [])

    def test_long_option_argument_split(self):
        self.assertParseOK(["--boo", "111"],
                           {'a': None, 'boo': 111, 'foo': None},
                           [])

    def test_long_option_short_option(self):
        self.assertParseOK(["--foo=bar", "-axyz"],
                           {'a': 'xyz', 'boo': None, 'foo': ["bar"]},
                           [])

    def test_abbrev_long_option(self):
        self.assertParseOK(["--f=bar", "-axyz"],
                           {'a': 'xyz', 'boo': None, 'foo': ["bar"]},
                           [])

    def test_defaults(self):
        (options, args) = self.parser.parse_args([])
        defaults = self.parser.get_default_values()
        self.assertEqual(vars(defaults), vars(options))

    def test_ambiguous_option(self):
        self.parser.add_option("--foz", action="store",
                               type="string", dest="foo")
        self.assertParseFail(["--f=bar"],
                             "ambiguous option: --f (--foo, --foz?)")


    def test_short_and_long_option_split(self):
        self.assertParseOK(["-a", "xyz", "--foo", "bar"],
                           {'a': 'xyz', 'boo': None, 'foo': ["bar"]},
                           []),

    def test_short_option_split_long_option_append(self):
        self.assertParseOK(["--foo=bar", "-b", "123", "--foo", "baz"],
                           {'a': None, 'boo': 123, 'foo': ["bar", "baz"]},
                           [])

    def test_short_option_split_one_positional_arg(self):
        self.assertParseOK(["-a", "foo", "bar"],
                           {'a': "foo", 'boo': None, 'foo': None},
                           ["bar"]),

    def test_short_option_consumes_separator(self):
        self.assertParseOK(["-a", "--", "foo", "bar"],
                           {'a': "--", 'boo': None, 'foo': None},
                           ["foo", "bar"]),
        self.assertParseOK(["-a", "--", "--foo", "bar"],
                           {'a': "--", 'boo': None, 'foo': ["bar"]},
                           []),

    def test_short_option_joined_and_separator(self):
        self.assertParseOK(["-ab", "--", "--foo", "bar"],
                           {'a': "b", 'boo': None, 'foo': None},
                           ["--foo", "bar"]),

    def test_hyphen_becomes_positional_arg(self):
        self.assertParseOK(["-ab", "-", "--foo", "bar"],
                           {'a': "b", 'boo': None, 'foo': ["bar"]},
                           ["-"])

    def test_no_append_versus_append(self):
        self.assertParseOK(["-b3", "-b", "5", "--foo=bar", "--foo", "baz"],
                           {'a': None, 'boo': 5, 'foo': ["bar", "baz"]},
                           [])

    def test_option_consumes_optionlike_string(self):
        self.assertParseOK(["-a", "-b3"],
                           {'a': "-b3", 'boo': None, 'foo': None},
                           [])

    def test_combined_single_invalid_option(self):
        self.parser.add_option("-t", action="store_true")
        self.assertParseFail(["-test"],
                             "no such option: -e")

    def test_add_option_accepts_unicode(self):
        self.parser.add_option(u"-u", u"--unicode", action="store_true")
        self.assertParseOK(["-u"],
                           {'a': None, 'boo': None, 'foo': None, 'unicode': True},
                           [])


class TestBool(BaseTest):
    def setUp(self):
        options = [make_option("-v",
                               "--verbose",
                               action="store_true",
                               dest="verbose",
                               default=''),
                   make_option("-q",
                               "--quiet",
                               action="store_false",
                               dest="verbose")]
        self.parser = OptionParser(option_list = options)

    def test_bool_default(self):
        self.assertParseOK([],
                           {'verbose': ''},
                           [])

    def test_bool_false(self):
        (options, args) = self.assertParseOK(["-q"],
                                             {'verbose': 0},
                                             [])
        self.assertTrue(options.verbose is False)

    def test_bool_true(self):
        (options, args) = self.assertParseOK(["-v"],
                                             {'verbose': 1},
                                             [])
        self.assertTrue(options.verbose is True)

    def test_bool_flicker_on_and_off(self):
        self.assertParseOK(["-qvq", "-q", "-v"],
                           {'verbose': 1},
                           [])

class TestChoice(BaseTest):
    def setUp(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
        self.parser.add_option("-c", action="store", type="choice",
                               dest="choice", choices=["one", "two", "three"])

    def test_valid_choice(self):
        self.assertParseOK(["-c", "one", "xyz"],
                           {'choice': 'one'},
                           ["xyz"])

    def test_invalid_choice(self):
        self.assertParseFail(["-c", "four", "abc"],
                             "option -c: invalid choice: 'four' "
                             "(choose from 'one', 'two', 'three')")

    def test_add_choice_option(self):
        self.parser.add_option("-d", "--default",
                               choices=["four", "five", "six"])
        opt = self.parser.get_option("-d")
        self.assertEqual(opt.type, "choice")
        self.assertEqual(opt.action, "store")

class TestCount(BaseTest):
    def setUp(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
        self.v_opt = make_option("-v", action="count", dest="verbose")
        self.parser.add_option(self.v_opt)
        self.parser.add_option("--verbose", type="int", dest="verbose")
        self.parser.add_option("-q", "--quiet",
                               action="store_const", dest="verbose", const=0)

    def test_empty(self):
        self.assertParseOK([], {'verbose': None}, [])

    def test_count_one(self):
        self.assertParseOK(["-v"], {'verbose': 1}, [])

    def test_count_three(self):
        self.assertParseOK(["-vvv"], {'verbose': 3}, [])

    def test_count_three_apart(self):
        self.assertParseOK(["-v", "-v", "-v"], {'verbose': 3}, [])

    def test_count_override_amount(self):
        self.assertParseOK(["-vvv", "--verbose=2"], {'verbose': 2}, [])

    def test_count_override_quiet(self):
        self.assertParseOK(["-vvv", "--verbose=2", "-q"], {'verbose': 0}, [])

    def test_count_overriding(self):
        self.assertParseOK(["-vvv", "--verbose=2", "-q", "-v"],
                           {'verbose': 1}, [])

    def test_count_interspersed_args(self):
        self.assertParseOK(["--quiet", "3", "-v"],
                           {'verbose': 1},
                           ["3"])

    def test_count_no_interspersed_args(self):
        self.parser.disable_interspersed_args()
        self.assertParseOK(["--quiet", "3", "-v"],
                           {'verbose': 0},
                           ["3", "-v"])

    def test_count_no_such_option(self):
        self.assertParseFail(["-q3", "-v"], "no such option: -3")

    def test_count_option_no_value(self):
        self.assertParseFail(["--quiet=3", "-v"],
                             "--quiet option does not take a value")

    def test_count_with_default(self):
        self.parser.set_default('verbose', 0)
        self.assertParseOK([], {'verbose':0}, [])

    def test_count_overriding_default(self):
        self.parser.set_default('verbose', 0)
        self.assertParseOK(["-vvv", "--verbose=2", "-q", "-v"],
                           {'verbose': 1}, [])

class TestMultipleArgs(BaseTest):
    def setUp(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
        self.parser.add_option("-p", "--point",
                               action="store", nargs=3, type="float", dest="point")

    def test_nargs_with_positional_args(self):
        self.assertParseOK(["foo", "-p", "1", "2.5", "-4.3", "xyz"],
                           {'point': (1.0, 2.5, -4.3)},
                           ["foo", "xyz"])

    def test_nargs_long_opt(self):
        self.assertParseOK(["--point", "-1", "2.5", "-0", "xyz"],
                           {'point': (-1.0, 2.5, -0.0)},
                           ["xyz"])

    def test_nargs_invalid_float_value(self):
        self.assertParseFail(["-p", "1.0", "2x", "3.5"],
                             "option -p: "
                             "invalid floating-point value: '2x'")

    def test_nargs_required_values(self):
        self.assertParseFail(["--point", "1.0", "3.5"],
                             "--point option requires 3 arguments")

class TestMultipleArgsAppend(BaseTest):
    def setUp(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
        self.parser.add_option("-p", "--point", action="store", nargs=3,
                               type="float", dest="point")
        self.parser.add_option("-f", "--foo", action="append", nargs=2,
                               type="int", dest="foo")
        self.parser.add_option("-z", "--zero", action="append_const",
                               dest="foo", const=(0, 0))

    def test_nargs_append(self):
        self.assertParseOK(["-f", "4", "-3", "blah", "--foo", "1", "666"],
                           {'point': None, 'foo': [(4, -3), (1, 666)]},
                           ["blah"])

    def test_nargs_append_required_values(self):
        self.assertParseFail(["-f4,3"],
                             "-f option requires 2 arguments")

    def test_nargs_append_simple(self):
        self.assertParseOK(["--foo=3", "4"],
                           {'point': None, 'foo':[(3, 4)]},
                           [])

    def test_nargs_append_const(self):
        self.assertParseOK(["--zero", "--foo", "3", "4", "-z"],
                           {'point': None, 'foo':[(0, 0), (3, 4), (0, 0)]},
                           [])

class TestVersion(BaseTest):
    def test_version(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE,
                                               version="%prog 0.1")
        save_argv = sys.argv[:]
        try:
            sys.argv[0] = os.path.join(os.curdir, "foo", "bar")
            self.assertOutput(["--version"], "bar 0.1\n")
        finally:
            sys.argv[:] = save_argv

    def test_no_version(self):
        self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
        self.assertParseFail(["--version"],
                             "no such option: --version")

# -- Test conflicting default values and parser.parse_args() -----------

class TestConflictingDefaults(BaseTest):
    """Conflicting default values: the last one should win."""
    def setUp(self):
        self.parser = OptionParser(option_list=[
            make_option("-v", action="store_true", dest="verbose", default=1)])
