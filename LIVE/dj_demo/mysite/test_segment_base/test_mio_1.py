# generator for load tests
def test_load():
    for case in case_table4 + case_table5:
        name = case['name']
        expected = case['expected']
        filt = pjoin(test_data_path, 'test%s_*.mat' % name)
        files = glob(filt)
        assert_true(len(files) > 0,
                    "No files for test %s using filter %s" % (name, filt))
        yield _load_check_case, name, files, expected
