# A convenient entry-point - if used, 'SKIPPED' exceptions will be supressed.
def testmain(*args, **kw):
    new_kw = kw.copy()
    if 'testLoader' not in new_kw:
        new_kw['testLoader'] = TestLoader()
    program_class = new_kw.get('testProgram', TestProgram)
    program_class(*args, **new_kw)
