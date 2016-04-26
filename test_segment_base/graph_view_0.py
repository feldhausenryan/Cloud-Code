#    @on_trait_change('nodes.+')
    def node_changed(self, name, obj, old, new):
        print "node changed"
        self._canvas.request_redraw()
