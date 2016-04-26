# Make a new buffer suitable for querying an items attributes.
def EmptyLVITEM(item, subitem, mask = None, text_buf_size=512):
    extra = [] # objects we must keep references to
    if mask is None:
        mask = commctrl.LVIF_IMAGE | commctrl.LVIF_INDENT | commctrl.LVIF_TEXT | \
               commctrl.LVIF_PARAM | commctrl.LVIF_STATE
    if mask & commctrl.LVIF_TEXT:
        text_buffer = _make_empty_text_buffer(text_buf_size)
        extra.append(text_buffer)
        text_addr, _ = text_buffer.buffer_info()
    else:
        text_addr = text_buf_size = 0
    buf = struct.pack(_lvitem_fmt,
                      mask, item, subitem, 
                      0, 0,
                      text_addr, text_buf_size, # text
                      0, 0, 0)
    return array.array("b", buf), extra
