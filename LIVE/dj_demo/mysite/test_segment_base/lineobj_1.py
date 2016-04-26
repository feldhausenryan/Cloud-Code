########### Transpose
    def transpose_chars(self):
        p2 = Point(self)
        if p2 == 0:
            return
        elif p2 == len(self):
            p2 = p2 - 1
        p1 = p2 - 1
        self[p2], self[p1] = self[p1], self[p2]
        self.point = p2 + 1
