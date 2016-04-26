# Ask permission to download a file.
def askabout(filetype, filename, pwd):
    prompt = 'Retrieve %s %s from %s ? [ny] ' % (filetype, filename, pwd)
    while 1:
        reply = raw_input(prompt).strip().lower()
        if reply in ['y', 'ye', 'yes']:
            return 1
        if reply in ['', 'n', 'no', 'nop', 'nope']:
            return 0
        print 'Please answer yes or no.'
