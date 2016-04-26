# Install/Uninstall ------
def install(file=None, scriptlist=[], other=[]):
    if file:
        create_log_file(file)
    install_scripts(scriptlist)
    if other:
        if not isinstance(other,list):
            other = [other]
        for package_name in other:
            for suffix in POSTINSTALL_SUFFIX:
                os.chdir( os.path.dirname(file) )
                post_install = package_name+suffix
                if os.path.exists(post_install):
                    print "Executing %s post-install script..." % package_name,
                    print "( %s )" % post_install,
                    os.system(post_install+' -install')
                    print "OK"
    print "\n\nPost-install script has been successfully executed."
