##########################################################################
# Color transfer function related utility code from MayaVi1.
##########################################################################
def _err_msg(obj, cls_name):
    return '%s %s does not have either a "nodes" attribute or a '\
           '"get_node_value" method'%(cls_name, str(obj))
