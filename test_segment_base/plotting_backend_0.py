# Functions
def compute_particles(number):
    x = N.random.standard_normal(number)
    y = N.random.standard_normal(number)
    px = N.random.standard_normal(number)
    py = N.random.standard_normal(number)
    return x, y, px, py
