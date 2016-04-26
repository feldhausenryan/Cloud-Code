# the main entry point for users...
def draw(drawing, canvas, x=0, y=0, showBoundary=rl_config.showBoundary):
    """As it says"""
    R = _PSRenderer()
    R.draw(renderScaledDrawing(drawing), canvas, x, y, showBoundary=showBoundary)
