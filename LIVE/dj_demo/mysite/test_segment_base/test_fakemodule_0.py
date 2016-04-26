# Make a fakemod and check a few properties
def test_mk_fakemod():
    fm = FakeModule()
    yield nt.assert_true,fm
    yield nt.assert_true,lambda : hasattr(fm,'__file__')
