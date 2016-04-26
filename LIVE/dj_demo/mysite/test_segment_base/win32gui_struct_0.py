# make an 'empty' buffer, ready for filling with cch characters.
def _make_empty_text_buffer(cch):
    return _make_text_buffer("\0" * cch)
