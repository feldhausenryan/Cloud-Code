# Round trip tests
def _rt_check_case(name, expected, format):
    mat_stream = BytesIO()
    savemat_future(mat_stream, expected, format=format)
    mat_stream.seek(0)
    _load_check_case(name, [mat_stream], expected)
