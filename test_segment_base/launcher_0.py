# This is only used on Windows.
def find_job_cmd():
    if WINDOWS:
        try:
            return find_cmd('job')
        except (FindCmdError, ImportError):
            # ImportError will be raised if win32api is not installed
            return 'job'
    else:
        return 'job'
