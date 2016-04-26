# Test each kind of 'except' line.
def no_jump_to_except_1(output):
    try:
        output.append(2)
    except:
        e = sys.exc_info()[1]
        output.append('except' in str(e))
