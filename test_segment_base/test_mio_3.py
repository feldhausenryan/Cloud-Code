# generator for round trip tests
def test_round_trip():
    for case in case_table4 + case_table5_rt:
        name = case['name'] + '_round_trip'
        expected = case['expected']
        format = case in case_table4 and '4' or '5'
        yield _rt_check_case, name, expected, format
