### Movement with extend selection
    def beginning_of_line_extend_selection(self, e): # 
        """Move to the start of the current line. """
        self.l_buffer.beginning_of_line_extend_selection()
        self.finalize()
