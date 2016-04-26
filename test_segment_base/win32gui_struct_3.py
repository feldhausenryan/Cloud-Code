# Make a new buffer suitable for querying hitem's attributes.
def EmptyTVITEM(hitem, mask = None, text_buf_size=512):
    extra = [] # objects we must keep references to
    if mask is None:
        mask = commctrl.TVIF_HANDLE | commctrl.TVIF_STATE | commctrl.TVIF_TEXT | \
               commctrl.TVIF_IMAGE | commctrl.TVIF_SELECTEDIMAGE | \
               commctrl.TVIF_CHILDREN | commctrl.TVIF_PARAM
    if mask & commctrl.TVIF_TEXT:
        text_buffer = _make_empty_text_buffer(text_buf_size)
        extra.append(text_buffer)
        text_addr, _ = text_buffer.buffer_info()
    else:
        text_addr = text_buf_size = 0
    buf = struct.pack(_tvitem_fmt,
                      mask, hitem,
                      0, 0,
                      text_addr, text_buf_size, # text
                      0, 0,
                      0, 0)
    return array.array("b", buf), extra
