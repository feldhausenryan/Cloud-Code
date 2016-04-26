# line 40
    def argue(self, a, b, c):
        try:
            spam(a, b, c)
        except:
            self.ex = sys.exc_info()
            self.tr = inspect.trace()
