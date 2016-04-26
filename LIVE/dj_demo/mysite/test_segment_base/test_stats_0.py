##    def test_dtype(self):
##        ''' Test a 1d list with a new dtype'''
##        a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##        b = 45.2872868812
##        self.do(a, b, dtype=np.float128)  # does not exist on win32
    def test_1dlist0(self):
        ''' Test a 1d list with zero element'''
        a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 0]
        b = 0.0 # due to exp(-inf)=0
        olderr = np.seterr(all='ignore')
        try:
            self.do(a, b)
        finally:
            np.seterr(**olderr)
