######################################################################
# The scene icon.
######################################################################
def mk_scene_icon():
    icon_path = os.path.join(resource_path(), 'images', 'scene.ico')
    return ImageResource(icon_path)
