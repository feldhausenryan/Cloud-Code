'''
        astng = builder.string_build(code, __name__, __file__)
        self.assertEqual(len(list(astng['process_line'].infer_call_result(
                                                                None))), 3)
        self.assertEqual(len(list(astng['tupletest'].infer())), 3)
        values = ['Function(first_word)', 'Function(last_word)', 'Const(NoneType)']
        self.assertEqual([str(infered)
                          for infered in astng['fct'].infer()], values)

    def test_float_complex_ambiguity(self):
        code = '''
def no_conjugate_member(magic_flag):
    """should not raise E1101 on something.conjugate"""
    if magic_flag:
        something = 1.0
    else:
        something = 1.0j
    if isinstance(something, float):
        return something
    return something.conjugate()
        '''
        astng = builder.string_build(code, __name__, __file__)
        self.assertEqual([i.value for i in
            astng['no_conjugate_member'].ilookup('something')], [1.0, 1.0j])
        self.assertEqual([i.value for i in
                get_name_node(astng, 'something', -1).infer()], [1.0, 1.0j])
    def test_lookup_cond_branches(self):
        code = '''
