# This verifies the line-numbers-must-be-integers rule.
def no_jump_to_non_integers(output):
    try:
        output.append(2)
    except ValueError, e:
        output.append('integer' in str(e))
