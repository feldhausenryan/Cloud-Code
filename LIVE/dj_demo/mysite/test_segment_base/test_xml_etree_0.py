# Only with Python implementation
def simplefind():
    """
    Test find methods using the elementpath fallback.
    >>> from xml.etree import ElementTree
    >>> CurrentElementPath = ElementTree.ElementPath
    >>> ElementTree.ElementPath = ElementTree._SimpleElementPath()
    >>> elem = ElementTree.XML(SAMPLE_XML)
    >>> elem.find("tag").tag
    'tag'
    >>> ElementTree.ElementTree(elem).find("tag").tag
    'tag'
    >>> elem.findtext("tag")
    'text'
    >>> elem.findtext("tog")
    >>> elem.findtext("tog", "default")
    'default'
    >>> ElementTree.ElementTree(elem).findtext("tag")
    'text'
    >>> summarize_list(elem.findall("tag"))
    ['tag', 'tag']
    >>> summarize_list(elem.findall(".//tag"))
    ['tag', 'tag', 'tag']
    Path syntax doesn't work in this case.
    >>> elem.find("section/tag")
    >>> elem.findtext("section/tag")
    >>> summarize_list(elem.findall("section/tag"))
    []
    >>> ElementTree.ElementPath = CurrentElementPath
    """
