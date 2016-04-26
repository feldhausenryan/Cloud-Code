######### Movement select
    def beginning_of_line_extend_selection(self):
        if self.enable_selection and self.selection_mark < 0:
            self.selection_mark = self.point
        self.point = StartOfLine
