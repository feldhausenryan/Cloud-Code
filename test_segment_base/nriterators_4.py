#
# Methods to check the correctness of the buffer structure
#
def zipBufferDescr(row, structure):
    """Zip a buffer row with its `descr` description.
    This function is used to check if buffers have a consistent format.
    This is done by applying the function on every row of the buffer.
    The function zips the buffer row with the buffer descr description
    in a recursive way, till a flat list of 2-tuples is obtained.
    Each 2-tuple contains the value of a field and its description.
    Recursion is needed to deal with nested fields of the buffer.
    This method assumes that descr description structure is good (i.e.
    that nestedrecords.checkDescr method raised no errors.).
    """
