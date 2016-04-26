# Executing the interpreter in a subprocess
def _assert_python(expected_success, *args, **env_vars):
    cmd_line = [sys.executable]
    if not env_vars:
        cmd_line.append('-E')
    cmd_line.extend(args)
    # Need to preserve the original environment, for in-place testing of
    # shared library builds.
    env = os.environ.copy()
    env.update(env_vars)
    p = subprocess.Popen(cmd_line, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         env=env)
    try:
        out, err = p.communicate()
    finally:
        subprocess._cleanup()
        p.stdout.close()
        p.stderr.close()
    rc = p.returncode
    err =  strip_python_stderr(err)
    if (rc and expected_success) or (not rc and not expected_success):
        raise AssertionError(
            "Process return code is %d, "
            "stderr follows:\n%s" % (rc, err.decode('ascii', 'ignore')))
    return rc, out, err
