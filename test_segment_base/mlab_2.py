##################################################
# Code related to things in and around polygons
##################################################
def inside_poly(points, verts):
    """
    *points* is a sequence of *x*, *y* points.
    *verts* is a sequence of *x*, *y* vertices of a polygon.
    Return value is a sequence of indices into points for the points
    that are inside the polygon.
    """
    # Make a closed polygon path
    poly = Path( verts )
    # Check to see which points are contained withing the Path
    return [ idx for idx, p in enumerate(points) if poly.contains_point(p) ]
