# ===================================================
# Image parameters
# ===================================================
def _create_choices():
    choices = []
    for cmap_name in get_colormap_list():
        choices.append((cmap_name, cmap_name, build_icon_from_cmap_name))
    return choices
