#--------------------------------------------------------------------------
# Return an HTML table with selected item in a special class
#--------------------------------------------------------------------------
def html_tableify(item_matrix, select=None, header=None , footer=None) :
    """ returnr a string for an html table"""
    if not item_matrix :
        return ''
    html_cols = []
    tds = lambda text : u'<td>'+text+u'  </td>'
    trs = lambda text : u'<tr>'+text+u'</tr>'
    tds_items = [map(tds, row) for row in item_matrix]
    if select :
        row, col = select
        tds_items[row][col] = u'<td class="inverted">'\
                +item_matrix[row][col]\
                +u'  </td>'
    #select the right item
    html_cols = map(trs, (u''.join(row) for row in tds_items))
    head = ''
    foot = ''
    if header :
        head = (u'<tr>'\
            +''.join((u'<td>'+header+u'</td>')*len(item_matrix[0]))\
            +'</tr>')
    if footer : 
        foot = (u'<tr>'\
            +''.join((u'<td>'+footer+u'</td>')*len(item_matrix[0]))\
            +'</tr>')
    html = (u'<table class="completion" style="white-space:pre">'+head+(u''.join(html_cols))+foot+u'</table>')
    return html
