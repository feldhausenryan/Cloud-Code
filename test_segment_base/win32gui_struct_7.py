# Make a new buffer suitable for querying an items attributes.
def EmptyLVCOLUMN(mask = None, text_buf_size=512):
    extra = [] # objects we must keep references to
    if mask is None:
        mask = commctrl.LVCF_FMT | commctrl.LVCF_WIDTH | commctrl.LVCF_TEXT | \
               commctrl.LVCF_SUBITEM | commctrl.LVCF_IMAGE | commctrl.LVCF_ORDER
    if mask & commctrl.LVCF_TEXT:
        text_buffer = _make_empty_text_buffer(text_buf_size)
        extra.append(text_buffer)
        text_addr, _ = text_buffer.buffer_info()
    else:
        text_addr = text_buf_size = 0
    buf = struct.pack(_lvcolumn_fmt,
                      mask, 0, 0,
                      text_addr, text_buf_size, # text
                      0, 0, 0)
    return array.array("b", buf), extra
