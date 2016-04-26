#TODO: The following functions (title, xlabel, ...) should update an already 
#      shown figure to be compatible with interactive mode -- for now it just 
#      works if these functions are called before showing the figure
def title(text):
    """Set current figure title"""
    global _figures
    fig = gcf()
    _figures.pop(fig.title)
    fig.title = text
    _figures[text] = fig
