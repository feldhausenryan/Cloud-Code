#-----------------------------------------------------------------------------
# Functions and class declarations
#-----------------------------------------------------------------------------
def block_parser(part, rgxin, rgxout, fmtin, fmtout):
    """
    part is a string of ipython text, comprised of at most one
    input, one ouput, comments, and blank lines.  The block parser
    parses the text into a list of::
      blocks = [ (TOKEN0, data0), (TOKEN1, data1), ...]
    where TOKEN is one of [COMMENT | INPUT | OUTPUT ] and
    data is, depending on the type of token::
      COMMENT : the comment string
      INPUT: the (DECORATOR, INPUT_LINE, REST) where
         DECORATOR: the input decorator (or None)
         INPUT_LINE: the input as string (possibly multi-line)
         REST : any stdout generated by the input line (not OUTPUT)
      OUTPUT: the output string, possibly multi-line
    """
    block = []
    lines = part.split('\n')
    N = len(lines)
    i = 0
    decorator = None
    while 1:
        if i==N:
            # nothing left to parse -- the last line
            break
        line = lines[i]
        i += 1
        line_stripped = line.strip()
        if line_stripped.startswith('#'):
            block.append((COMMENT, line))
            continue
        if line_stripped.startswith('@'):
            # we're assuming at most one decorator -- may need to
            # rethink
            decorator = line_stripped
            continue
        # does this look like an input line?
        matchin = rgxin.match(line)
        if matchin:
            lineno, inputline = int(matchin.group(1)), matchin.group(2)
            # the ....: continuation string
            continuation = '   %s:'%''.join(['.']*(len(str(lineno))+2))
            Nc = len(continuation)
            # input lines can continue on for more than one line, if
            # we have a '\' line continuation char or a function call
            # echo line 'print'.  The input line can only be
            # terminated by the end of the block or an output line, so
            # we parse out the rest of the input line if it is
            # multiline as well as any echo text
            rest = []
            while i<N:
                # look ahead; if the next line is blank, or a comment, or
                # an output line, we're done
                nextline = lines[i]
                matchout = rgxout.match(nextline)
                #print "nextline=%s, continuation=%s, starts=%s"%(nextline, continuation, nextline.startswith(continuation))
                if matchout or nextline.startswith('#'):
                    break
                elif nextline.startswith(continuation):
                    inputline += '\n' + nextline[Nc:]
                else:
                    rest.append(nextline)
                i+= 1
            block.append((INPUT, (decorator, inputline, '\n'.join(rest))))
            continue
        # if it looks like an output line grab all the text to the end
        # of the block
        matchout = rgxout.match(line)
        if matchout:
            lineno, output = int(matchout.group(1)), matchout.group(2)
            if i<N-1:
                output = '\n'.join([output] + lines[i:])
            block.append((OUTPUT, output))
            break
    return block
