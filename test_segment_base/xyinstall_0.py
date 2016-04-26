# Windows registry ------
def get_package_name(filename):
    package_name = os.path.split(filename)[1]
    for suffix in POSTINSTALL_SUFFIX:
        package_name = package_name.replace(suffix,'')
    return package_name
