#
# Unregister info is for installers or external uninstallers.
# The WISE installer, for example firstly registers the COM server,
# then queries for the Unregister info, appending it to its
# install log.  Uninstalling the package will the uninstall the server
def UnregisterInfoClasses(*classes, **flags):
  ret = []
  for cls in classes:
    clsid = cls._reg_clsid_
    progID = _get(cls, '_reg_progid_')
    verProgID = _get(cls, '_reg_verprogid_')
    customKeys = _get(cls, '_reg_remove_keys_')
    ret = ret + GetUnregisterServerKeys(clsid, progID, verProgID, customKeys)
  return ret
