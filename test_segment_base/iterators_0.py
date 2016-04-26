# This function will become a method of the Message class
def walk(self):
    """Walk over the message tree, yielding each subpart.
    The walk is performed in depth-first order.  This method is a
    generator.
    """
    yield self
    if self.is_multipart():
        for subpart in self.get_payload():
            for subsubpart in subpart.walk():
                yield subsubpart
