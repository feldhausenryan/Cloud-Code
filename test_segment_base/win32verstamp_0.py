#
# Set VS_FF_PRERELEASE and DEBUG if Debug
#
def file_flags(debug):
  if debug:
    return 3	# VS_FF_DEBUG | VS_FF_PRERELEASE
  return 0
