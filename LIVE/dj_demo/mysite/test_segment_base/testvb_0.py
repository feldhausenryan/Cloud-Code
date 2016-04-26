# Make this test run under our test suite to leak tests etc work
def suite():
    import unittest
    test = util.CapturingFunctionTestCase(TestAll, description="VB tests")
    suite = unittest.TestSuite()
    suite.addTest(test)
    return suite
