'''
        astng = builder.string_build(code, __name__, __file__)
        infered = list(get_name_node(astng, 'a').infer())

        self.assertEqual(len(infered), 1)
        self.assertIsInstance(infered[0], nodes.Const)
        self.assertEqual(infered[0].value, 3)

    def test_nonregr_func_arg(self):
        code = '''
def foo(self, bar):
    def baz():
        pass
    def qux():
        return baz
    spam = bar(None, qux)
    print (spam)
