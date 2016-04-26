#-----
# Misc
#-----
def basic_stats(data):
    nbfac = data.size * 1. / (data.size - 1)
    return np.nanmin(data), np.nanmax(data), np.mean(data), np.std(data) * nbfac
