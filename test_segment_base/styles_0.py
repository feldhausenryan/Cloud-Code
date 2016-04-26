# ===================================================
# Common font parameters
# ===================================================
def _font_selection(param, item, value, parent):
    font = param.build_font()
    result, valid = QFontDialog.getFont(font, parent)
    if valid:
        param.update_param( result )
