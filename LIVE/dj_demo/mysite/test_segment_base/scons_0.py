# A few notes:
#   - numscons is not mandatory to build numpy, so we cannot import it here.
#   Any numscons import has to happen once we check numscons is available and
#   is required for the build (call through setupscons.py or native numscons
#   build).
def get_scons_build_dir():
    """Return the top path where everything produced by scons will be put.
    The path is relative to the top setup.py"""
    from numscons import get_scons_build_dir
    return get_scons_build_dir()
