# Service Principal Names functions from the same sample.
# The example calls the DsWriteAccountSpn function, which stores the SPNs in
# Microsoft Active Directory under the servicePrincipalName attribute of the
# account object specified by the serviceAcctDN parameter. The account object
# corresponds to the logon account specified in the CreateService call for this
# service instance. If the logon account is a domain user account,
# serviceAcctDN must be the distinguished name of the account object in
# Active Directory for that user account. If the service's logon account is the
# LocalSystem account, serviceAcctDN must be the distinguished name of the
# computer account object for the host computer on which the service is
# installed. win32api.TranslateNames and win32security.DsCrackNames can
# be used to convert a domain\account format name to a distinguished name.
def SpnRegister(
        serviceAcctDN,    # DN of the service's logon account
        spns,             # List of SPNs to register
        operation,         # Add, replace, or delete SPNs
           ):
    assert type(spns) not in [str, unicode] and hasattr(spns, "__iter__"), \
           "spns must be a sequence of strings (got %r)" % spns
    # Bind to a domain controller. 
    # Get the domain for the current user.
    samName = win32api.GetUserNameEx(win32api.NameSamCompatible)
    samName = samName.split('\\', 1)[0]
    if not serviceAcctDN:
        # Get the SAM account name of the computer object for the server.
        serviceAcctDN = win32api.GetComputerObjectName(win32con.NameFullyQualifiedDN)
    logger.debug("SpnRegister using DN '%s'", serviceAcctDN)
    # Get the name of a domain controller in that domain.
    info = win32security.DsGetDcName(
                domainName=samName,
                flags=dscon.DS_IS_FLAT_NAME |
                      dscon.DS_RETURN_DNS_NAME |
                      dscon.DS_DIRECTORY_SERVICE_REQUIRED)
    # Bind to the domain controller.
    handle = win32security.DsBind( info['DomainControllerName'] )
    # Write the SPNs to the service account or computer account.
    logger.debug("DsWriteAccountSpn with spns %s")
    win32security.DsWriteAccountSpn(
            handle,         # handle to the directory
            operation,   # Add or remove SPN from account's existing SPNs
            serviceAcctDN,        # DN of service account or computer account
            spns) # names
    # Unbind the DS in any case (but Python would do it anyway)
    handle.Close()
