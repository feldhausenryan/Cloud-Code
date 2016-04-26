# Returns distinguished name of SCP.
def ScpCreate(
    service_binding_info, 
    service_class_name,      # Service class string to store in SCP.
    account_name = None,    # Logon account that needs access to SCP.
    container_name = None,
    keywords = None,
    object_class = "serviceConnectionPoint",
    dns_name_type = "A",
    dn = None,
    dns_name = None,
             ):
    container_name = container_name or service_class_name
    if not dns_name:
        # Get the DNS name of the local computer
        dns_name = win32api.GetComputerNameEx(win32con.ComputerNameDnsFullyQualified)
    # Get the distinguished name of the computer object for the local computer
    if dn is None:
        dn = win32api.GetComputerObjectName(win32con.NameFullyQualifiedDN)
    # Compose the ADSpath and bind to the computer object for the local computer
    comp = adsi.ADsGetObject("LDAP://" + dn, adsi.IID_IDirectoryObject)
    # Publish the SCP as a child of the computer object
    keywords = keywords or []
    # Fill in the attribute values to be stored in the SCP.
    attrs = [
        ("cn", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (container_name,)),
        ("objectClass", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (object_class,)),
        ("keywords", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, keywords),
        ("serviceDnsName", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (dns_name,)),
        ("serviceDnsNameType", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (dns_name_type,)),
        ("serviceClassName", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (service_class_name,)),
        ("serviceBindingInformation", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (service_binding_info,)),
    ]
    new = comp.CreateDSObject("cn=" + container_name, attrs)
    logger.info("New connection point is at %s", container_name)
    # Wrap in a usable IDispatch object.
    new = Dispatch(new)
    # And allow access to the SCP for the specified account name
    AllowAccessToScpProperties(account_name, new)
    return new
