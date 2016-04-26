# the main entry point for users...
def draw(drawing, canvas, x, y, showBoundary=rl_config._unset_):
    """As it says"""
    R = _PMRenderer()
    R.draw(renderScaledDrawing(drawing), canvas, x, y, showBoundary=showBoundary)
