# utility
def write_header(f, text, char='-'):
    f.write(text + '\n')
    f.write(char * len(text) + '\n')
