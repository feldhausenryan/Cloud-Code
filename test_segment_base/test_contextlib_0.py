# This is needed to make the test actually run under regrtest.py!
def test_main():
    with test_support.check_warnings(("With-statements now directly support "
                                      "multiple context managers",
                                      DeprecationWarning)):
        test_support.run_unittest(__name__)
