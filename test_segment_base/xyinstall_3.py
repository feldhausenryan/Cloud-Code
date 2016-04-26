# Scripts ------
def copy_script( raw, py, exe ):
    '''fixes the python executable line if exists'''
    first_line_re = re.compile('^#!.*python[0-9.]*\s*')
    f = open(raw, "r")
    first_line = f.readline()
    match = first_line_re.match(first_line)
    if match:
        outf = open(py, "w")
        outf.write("#!%s\n" % (exe))
        outf.writelines(f.readlines())
        outf.close()
        f.close()
    else:
        f.close()
        shutil.copy(raw, py)
