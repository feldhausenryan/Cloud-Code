# A special function for use with the matplotlib FuncFormatter class
# for formatting axes with radian units.
# This was copied from matplotlib example code.
def rad_fn(x, pos = None ):
   """Radian function formatter."""
   n = int((x / np.pi) * 2.0 + 0.25)
   if n == 0:
      return str(x)
   elif n == 1:
      return r'$\pi/2$'
   elif n == 2:
      return r'$\pi$'
   elif n % 2 == 0:
      return r'$%s\pi$' % (n/2,)
   else:
      return r'$%s\pi/2$' % (n,)
