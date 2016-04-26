'''
        astng = builder.string_build(code, __name__, __file__)
        callfuncnode = astng['f'].body[0].value.expr
        infered = list(callfuncnode.infer())
        self.assertEqual(len(infered), 2, infered)
        infered.remove(YES)
        self.assertIsInstance(infered[0], nodes.Const)
        self.assertIsNone(infered[0].value)

    def test_nonregr_getitem_empty_tuple(self):
        code = '''
def f(x):
        a = ()[x]
        '''
        astng = builder.string_build(code, __name__, __file__)
        infered = list(astng['f'].ilookup('a'))
        self.assertEqual(len(infered), 1)
        self.assertEqual(infered[0], YES)
    def test_python25_generator_exit(self):
        sys.stderr = StringIO()
        data = "b = {}[str(0)+''].a"
        astng = builder.string_build(data, __name__, __file__)
        list(astng['b'].infer())
        output = sys.stderr.getvalue()
        # I have no idea how to test for this in another way...
        self.assertNotIn("RuntimeError", output, "Exception exceptions.RuntimeError: 'generator ignored GeneratorExit' in <generator object> ignored")
        sys.stderr = sys.__stderr__
    def test_python25_relative_import(self):
        data = "from ...common import date; print (date)"
        # !! FIXME also this relative import would not work 'in real' (no __init__.py in test/)
        # the test works since we pretend we have a package by passing the full modname
        astng = builder.string_build(data, 'logilab.astng.test.unittest_inference', __file__)
        infered = get_name_node(astng, 'date').infer().next()
        self.assertIsInstance(infered, nodes.Module)
        self.assertEqual(infered.name, 'logilab.common.date')
    def test_python25_no_relative_import(self):
        fname = join(abspath(dirname(__file__)), 'regrtest_data', 'package', 'absimport.py')
        astng = builder.file_build(fname, 'absimport')
        self.assertTrue(astng.absolute_import_activated(), True)
        infered = get_name_node(astng, 'import_package_subpackage_module').infer().next()
        # failed to import since absolute_import is activated
        self.assertIs(infered, YES)
    def test_nonregr_absolute_import(self):
        fname = join(abspath(dirname(__file__)), 'regrtest_data', 'absimp', 'string.py')
        astng = builder.file_build(fname, 'absimp.string')
        self.assertTrue(astng.absolute_import_activated(), True)
        infered = get_name_node(astng, 'string').infer().next()
        self.assertIsInstance(infered, nodes.Module)
        self.assertEqual(infered.name, 'string')
        self.assertIn('ascii_letters', infered.locals)
    def test_mechanize_open(self):
        try:
            import mechanize
        except ImportError:
            self.skipTest('require mechanize installed')
        data = '''from mechanize import Browser
