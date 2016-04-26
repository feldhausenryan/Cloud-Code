# The dict of defaults
default_unit_converters = {
       "<class 'scimath.units.unit_array.UnitArray'>" :
                                                   convert_unit_array,
       "<class 'scimath.units.quantity.Quantity'>": convert_quantity,
       "<class 'scimath.units.scalar.Scalar'>": convert_quantity,
       "<class 'cp.log.log_index.LogIndex'>": convert_log_index,
       "<class 'cp.log.log.Log'>": convert_log,
       "<class 'cp.log.log_suite_proxy.LogProxy'>": convert_log,
       "<class 'cp.log.log_suite.LogSuite'>": convert_log_suite,
       "<class 'cp.lab.action_variable.ActionVariable'>":
                                                   convert_action_variable,
       "<class 'cp.log.editable_log_suite_proxy.EditableLogProxy'>":
                                                   convert_log_proxy,
       "<class 'cp.log.log_suite_proxy.LogSuiteProxy'>" : convert_log_proxy,
       }
