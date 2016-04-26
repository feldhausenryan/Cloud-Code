#----------------
# umath generator
#----------------
def do_generate_umath(targetfile, sourcefile, env):
    t = open(targetfile, 'w')
    from code_generators import generate_umath
    code = generate_umath.make_code(generate_umath.defdict, generate_umath.__file__)
    t.write(code)
    t.close()
