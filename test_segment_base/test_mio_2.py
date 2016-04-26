# generator for whos tests
def test_whos():
    for case in case_table4 + case_table5:
        name = case['name']
        expected = case['expected']
        classes = case['classes']
        filt = pjoin(test_data_path, 'test%s_*.mat' % name)
        files = glob(filt)
        assert_true(len(files) > 0,
                    "No files for test %s using filter %s" % (name, filt))
        yield _whos_check_case, name, files, expected, classes
