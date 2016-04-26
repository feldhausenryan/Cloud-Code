#########  History commands
    def previous_history(self, e):  # (C-p)
        '''Move back through the history list, fetching the previous
        command. '''
        self._history.previous_history(self.l_buffer)
        self.l_buffer.point = lineobj.EndOfLine
        self.finalize()
