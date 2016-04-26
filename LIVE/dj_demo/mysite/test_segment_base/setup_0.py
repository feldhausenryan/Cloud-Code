#!/usr/bin/env python
def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('contour',parent_package,top_path)
    numerix_info = config.get_info('numerix')
    config.add_extension('contour',['*.c'],**numerix_info)
    config.add_data_dir('tests')
    return config
