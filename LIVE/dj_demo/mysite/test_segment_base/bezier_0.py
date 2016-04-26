# FIXME spelling mistake in the name of the parameter ``tolerence``
def find_bezier_t_intersecting_with_closedpath(bezier_point_at_t,
                                               inside_closedpath,
                                               t0=0., t1=1., tolerence=0.01):
    """ Find a parameter t0 and t1 of the given bezier path which
    bounds the intersecting points with a provided closed
    path(*inside_closedpath*). Search starts from *t0* and *t1* and it
    uses a simple bisecting algorithm therefore one of the end point
    must be inside the path while the orther doesn't. The search stop
    when |t0-t1| gets smaller than the given tolerence.
    value for
    - bezier_point_at_t : a function which returns x, y coordinates at *t*
    - inside_closedpath : return True if the point is insed the path
    """
    # inside_closedpath : function
    start = bezier_point_at_t(t0)
    end = bezier_point_at_t(t1)
    start_inside = inside_closedpath(start)
    end_inside = inside_closedpath(end)
    if not xor(start_inside, end_inside):
        raise NonIntersectingPathException(
                "the segment does not seem to intersect with the path")
    while 1:
        # return if the distance is smaller than the tolerence
        if (start[0] - end[0]) ** 2 + \
           (start[1] - end[1]) ** 2 < tolerence ** 2:
            return t0, t1
        # calculate the middle point
        middle_t = 0.5 * (t0 + t1)
        middle = bezier_point_at_t(middle_t)
        middle_inside = inside_closedpath(middle)
        if xor(start_inside, middle_inside):
            t1 = middle_t
            end = middle
            end_inside = middle_inside
        else:
            t0 = middle_t
            start = middle
            start_inside = middle_inside
