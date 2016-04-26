#  Set defaultIsolationLevel on module level before creating the connection.
#   For example:
#   import adodbapi, ado_consts
#   adodbapi.adodbapi.defaultIsolationLevel=ado_consts.adXactBrowse"
#
#  Set defaultCursorLocation on module level before creating the connection.
# It may be one of the "adUse..." consts.
defaultCursorLocation = adc.adUseClient   # changed from adUseServer as of v 2.3.0
