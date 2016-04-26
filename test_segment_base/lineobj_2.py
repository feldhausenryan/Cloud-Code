############## Kill ring
    def add_to_kill_ring(self,txt):
        self.kill_ring = [txt]
        if kill_ring_to_clipboard:
            clipboard.SetClipboardText(txt.get_line_text())
