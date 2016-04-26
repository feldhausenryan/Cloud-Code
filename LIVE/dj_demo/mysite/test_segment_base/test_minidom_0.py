# The tests of DocumentType importing use these helpers to construct
# the documents to work with, since not all DOM builders actually
# create the DocumentType nodes.
def create_doc_without_doctype(doctype=None):
    return getDOMImplementation().createDocument(None, "doc", doctype)
