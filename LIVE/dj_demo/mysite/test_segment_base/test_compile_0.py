''' % ((longexpr,)*10)
        exec code
        self.assertEqual(f(5), 0)

    def test_complex_args(self):

        with test_support.check_py3k_warnings(
                ("tuple parameter unpacking has been removed", SyntaxWarning)):
            exec textwrap.dedent('''
        def comp_args((a, b)):
            return a,b
