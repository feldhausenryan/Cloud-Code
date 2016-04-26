# LaTeX to HTML translation stuff:
def latex2html(node, source):
    inline = isinstance(node.parent, nodes.TextElement)
    latex = node['latex']
    name = 'math-%s' % md5(latex).hexdigest()[-10:]
    destdir = os.path.join(setup.app.builder.outdir, '_images', 'mathmpl')
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    dest = os.path.join(destdir, '%s.png' % name)
    path = os.path.join(setup.app.builder.imgpath, 'mathmpl')
    depth = latex2png(latex, dest, node['fontset'])
    if inline:
        cls = ''
    else:
        cls = 'class="center" '
    if inline and depth != 0:
        style = 'style="position: relative; bottom: -%dpx"' % (depth + 1)
    else:
        style = ''
    return '<img src="%s/%s.png" %s%s/>' % (path, name, cls, style)
