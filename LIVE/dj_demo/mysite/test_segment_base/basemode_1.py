########
    def clear_screen(self, e): # (C-l)
        """Clear the screen and redraw the current line, leaving the current
        line at the top of the screen."""
        self.console.page()
        self.finalize()
