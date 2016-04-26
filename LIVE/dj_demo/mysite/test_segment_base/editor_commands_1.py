# Qt client's set_? method changes its values, then
# emits a signal which tells the JS editor to update
def set_text(self, text):
    self._text = text
    self.text_changed.emit(text)
