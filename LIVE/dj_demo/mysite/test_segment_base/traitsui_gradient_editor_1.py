##########################################################################
# Test case related code.
##########################################################################
def make_test_table(lut=False):
    from ctf import ColorTransferFunction, PiecewiseFunction
    if lut:
        table = tvtk.LookupTable()
        table.table_range = (255, 355)
        return table, None, None
    else:
        table = tvtk.VolumeProperty()
        ctf = ColorTransferFunction()
        mins, maxs = 255, 355
        ds = (maxs-mins)/4.0
        try:
            ctf.range = (mins, maxs)
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass
        ctf.add_rgb_point(mins,      0.00, 0.0, 1.00)
        ctf.add_rgb_point(mins+ds,   0.25, 0.5, 0.75)
        ctf.add_rgb_point(mins+2*ds, 0.50, 1.0, 0.50)
        ctf.add_rgb_point(mins+3*ds, 0.75, 0.5, 0.25)
        ctf.add_rgb_point(maxs,      1.00, 0.0, 0.00)
        otf = PiecewiseFunction()
        otf.add_point(255, 0.0)
        otf.add_point(355, 0.2)
        table.set_color(ctf)
        table.set_scalar_opacity(otf)
        return table, ctf, otf
