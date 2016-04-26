# Open a service given either it's long or short name.
def SmartOpenService(hscm, name, access):
    try:
        return win32service.OpenService(hscm, name, access)
    except win32api.error, details:
        if details.winerror not in [winerror.ERROR_SERVICE_DOES_NOT_EXIST,
                                    winerror.ERROR_INVALID_NAME]:
            raise
    name = win32service.GetServiceKeyName(hscm, name)
    return win32service.OpenService(hscm, name, access)
