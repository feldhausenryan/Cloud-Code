#-----------------------------------------------------------------------
# A dictionary that maps filename extensions to functions that map
# parameters old and new to a list that can be passed to Popen to
# convert files with that extension to png format.
def get_cache_dir():
   cache_dir = os.path.join(_get_configdir(), 'test_cache')
   if not os.path.exists(cache_dir):
      try:
         os.makedirs(cache_dir)
      except IOError:
         return None
   if not os.access(cache_dir, os.W_OK):
      return None
   return cache_dir
