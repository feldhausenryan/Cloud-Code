# For invocation through regrtest
def test_main():
    from bsddb import db
    from bsddb.test import test_all
    test_all.set_test_path_prefix(os.path.join(tempfile.gettempdir(),
                                 'z-test_bsddb3-%s' %
                                 os.getpid()))
    # Please leave this print in, having this show up in the buildbots
    # makes diagnosing problems a lot easier.
    print >>sys.stderr, db.DB_VERSION_STRING
    print >>sys.stderr, 'Test path prefix: ', test_all.get_test_path_prefix()
    try:
        run_unittest(test_all.suite(module_prefix='bsddb.test.',
                                    timing_check=TimingCheck))
    finally:
        # The only reason to remove db_home is in case if there is an old
        # one lying around.  This might be by a different user, so just
        # ignore errors.  We should always make a unique name now.
        try:
            test_all.remove_test_path_directory()
        except:
            pass
