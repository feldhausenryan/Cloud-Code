######################################################################
# Utility functions.
######################################################################
def find_file_data_type(file_name):
    "Parses the named file to see what type of data there is."
    r = tvtk.XMLFileReadTester(file_name=file_name)
    if r.test_read_file():
        return r.file_data_type
    else:
        error("File %s is not a valid VTK XML file!"%(file_name))
