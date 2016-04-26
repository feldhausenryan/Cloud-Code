#==============================================================================
# DICOM Private I/O functions
#==============================================================================
def _import_dcm():
    """DICOM Import function (checking for required libraries):
    DICOM support requires library `pydicom`"""
    import logging
    logger = logging.getLogger("pydicom")
    logger.setLevel(logging.CRITICAL)
    import dicom  # analysis:ignore
    logger.setLevel(logging.WARNING)
