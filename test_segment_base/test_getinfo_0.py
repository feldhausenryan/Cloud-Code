## Callback function invoked when progress information is updated
def progress(download_t, download_d, upload_t, upload_d):
    print "Total to download %d bytes, have %d bytes so far" % \
          (download_t, download_d)
