'''
        astng = builder.string_build(code, __name__, __file__)
        p1 = astng['p1'].infer().next()
        self.assertTrue(p1.getattr('__name__'))
        p2 = astng['p2'].infer().next()
        self.assertTrue(p2.getattr('__name__'))
        self.assertTrue(astng['NoName'].getattr('__name__'))
        p3 = astng['p3'].infer().next()
        self.assertRaises(NotFoundError, p3.getattr, '__name__')


    def test_function_module_special(self):
        astng = builder.string_build('''
def initialize(linter):
    """initialize linter with checkers in this package """
    package_load(linter, __path__[0])
        ''', 'data.__init__', 'data/__init__.py')
        path = [n for n in astng.nodes_of_class(nodes.Name) if n.name == '__path__'][0]
        self.assertEqual(len(path.lookup('__path__')[1]), 1)
    def test_builtin_lookup(self):
        self.assertEqual(builtin_lookup('__dict__')[1], ())
        intstmts = builtin_lookup('int')[1]
        self.assertEqual(len(intstmts), 1)
        self.assertIsInstance(intstmts[0], nodes.Class)
        self.assertEqual(intstmts[0].name, 'int')
        self.assertIs(intstmts[0], nodes.const_factory(1)._proxied)
    def test_decorator_arguments_lookup(self):
        code = '''
