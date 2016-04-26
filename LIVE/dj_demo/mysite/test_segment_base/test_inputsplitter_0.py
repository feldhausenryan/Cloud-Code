#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------
def test_spaces():
    tests = [('', 0),
             (' ', 1),
             ('\n', 0),
             (' \n', 1),
             ('x', 0),
             (' x', 1),
             ('  x',2),
             ('    x',4),
             # Note: tabs are counted as a single whitespace!
             ('\tx', 1),
             ('\t x', 2),
             ]
    tt.check_pairs(isp.num_ini_spaces, tests)