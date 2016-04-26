# Post-install log file ------
def get_log_filename(name):
    if os.path.exists(name): # name is a filename
        name = get_package_name(name)
    path = get_install_param(name)
    return os.path.join(path, 'post_install.log')
