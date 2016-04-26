#####--------------------------------------------------------------------------
#---- --- Filling options ---
#####--------------------------------------------------------------------------
# b: boolean - c: complex - f: floats - i: integer - O: object - S: string
default_filler = {'b': True,
                  'c' : 1.e20 + 0.0j,
                  'f' : 1.e20,
                  'i' : 999999,
                  'O' : '?',
                  'S' : 'N/A',
                  'u' : 999999,
                  'V' : '???',
                  'U' : 'N/A',
                  'M8[D]' : np.datetime64('NaT', 'D'),
                  'M8[us]' : np.datetime64('NaT', 'us')
                  }
