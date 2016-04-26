# Return a test suite all loaded with the tests we want to run
def make_test_suite(test_level = 1):
    suite = unittest.TestSuite()
    import_failures = []
    loader = TestLoader()
    for i in range(testLevel):
        for mod_name in unittest_modules[i]:
            mod, func = get_test_mod_and_func(mod_name, import_failures)
            if mod is None:
                continue
            if func is not None:
                test = CapturingFunctionTestCase(func, description=mod_name)
            else:
                if hasattr(mod, "suite"):
                    test = mod.suite()
                else:
                    test = loader.loadTestsFromModule(mod)
            assert test.countTestCases() > 0, "No tests loaded from %r" % mod
            suite.addTest(test)
        for cmd, output in output_checked_programs[i]:
            suite.addTest(ShellTestCase(cmd, output))
        for test_class in custom_test_cases[i]:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test_class))
    # other "normal" unittest modules.
    for i in range(testLevel):
        for mod_name in unittest_other_modules[i]:
            try:
                __import__(mod_name)
            except:
                import_failures.append((mod_name, sys.exc_info()[:2]))
                continue
            mod = sys.modules[mod_name]
            if hasattr(mod, "suite"):
                test = mod.suite()
            else:
                test = loader.loadTestsFromModule(mod)
            assert test.countTestCases() > 0, "No tests loaded from %r" % mod
            suite.addTest(test)
    return suite, import_failures
