##############################################################################
# Utility functions.
##############################################################################
def get_imayavi_engine(window):
    """Returns the MayaVi Engine given the Envisage worbench window.
    """
    return window.get_service(Engine)
