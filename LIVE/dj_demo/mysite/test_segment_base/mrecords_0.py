#    #......................................................
    def view(self, dtype=None, type=None):
        """Returns a view of the mrecarray."""
        # OK, basic copy-paste from MaskedArray.view...
        if dtype is None:
            if type is None:
                output = ndarray.view(self)
            else:
                output = ndarray.view(self, type)
        # Here again...
        elif type is None:
            try:
                if issubclass(dtype, ndarray):
                    output = ndarray.view(self, dtype)
                    dtype = None
                else:
                    output = ndarray.view(self, dtype)
            # OK, there's the change
            except TypeError:
                dtype = np.dtype(dtype)
                # we need to revert to MaskedArray, but keeping the possibility
                # ...of subclasses (eg, TimeSeriesRecords), so we'll force a type
                # ...set to the first parent
                if dtype.fields is None:
                    basetype = self.__class__.__bases__[0]
                    output = self.__array__().view(dtype, basetype)
                    output._update_from(self)
                else:
                    output = ndarray.view(self, dtype)
                output._fill_value = None
        else:
            output = ndarray.view(self, dtype, type)
        # Update the mask, just like in MaskedArray.view
        if (getattr(output, '_mask', nomask) is not nomask):
            mdtype = ma.make_mask_descr(output.dtype)
            output._mask = self._mask.view(mdtype, ndarray)
            output._mask.shape = output.shape
        return output
