#------------------------------------
# Ufunc and multiarray API generators
#------------------------------------
def do_generate_numpy_api(target, source, env):
    nowrap_do_generate_numpy_api([str(i) for i in target],
                                 [s.value for s in source])
    return 0
