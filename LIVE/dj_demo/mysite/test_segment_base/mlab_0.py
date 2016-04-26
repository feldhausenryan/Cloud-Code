#This is a helper function that implements the commonality between the
#psd, csd, and spectrogram.  It is *NOT* meant to be used outside of mlab
def _spectral_helper(x, y, NFFT=256, Fs=2, detrend=detrend_none,
        window=window_hanning, noverlap=0, pad_to=None, sides='default',
        scale_by_freq=None):
    #The checks for if y is x are so that we can use the same function to
    #implement the core of psd(), csd(), and spectrogram() without doing
    #extra calculations.  We return the unaveraged Pxy, freqs, and t.
    same_data = y is x
    #Make sure we're dealing with a numpy array. If y and x were the same
    #object to start with, keep them that way
    x = np.asarray(x)
    if not same_data:
        y = np.asarray(y)
    else:
        y = x
    # zero pad x and y up to NFFT if they are shorter than NFFT
    if len(x)<NFFT:
        n = len(x)
        x = np.resize(x, (NFFT,))
        x[n:] = 0
    if not same_data and len(y)<NFFT:
        n = len(y)
        y = np.resize(y, (NFFT,))
        y[n:] = 0
    if pad_to is None:
        pad_to = NFFT
    if scale_by_freq is None:
        scale_by_freq = True
    # For real x, ignore the negative frequencies unless told otherwise
    if (sides == 'default' and np.iscomplexobj(x)) or sides == 'twosided':
        numFreqs = pad_to
        scaling_factor = 1.
    elif sides in ('default', 'onesided'):
        numFreqs = pad_to//2 + 1
        scaling_factor = 2.
    else:
        raise ValueError("sides must be one of: 'default', 'onesided', or "
            "'twosided'")
    if cbook.iterable(window):
        assert(len(window) == NFFT)
        windowVals = window
    else:
        windowVals = window(np.ones((NFFT,), x.dtype))
    step = NFFT - noverlap
    ind = np.arange(0, len(x) - NFFT + 1, step)
    n = len(ind)
    Pxy = np.zeros((numFreqs, n), np.complex_)
    # do the ffts of the slices
    for i in range(n):
        thisX = x[ind[i]:ind[i]+NFFT]
        thisX = windowVals * detrend(thisX)
        fx = np.fft.fft(thisX, n=pad_to)
        if same_data:
            fy = fx
        else:
            thisY = y[ind[i]:ind[i]+NFFT]
            thisY = windowVals * detrend(thisY)
            fy = np.fft.fft(thisY, n=pad_to)
        Pxy[:,i] = np.conjugate(fx[:numFreqs]) * fy[:numFreqs]
    # Scale the spectrum by the norm of the window to compensate for
    # windowing loss; see Bendat & Piersol Sec 11.5.2.
    Pxy /= (np.abs(windowVals)**2).sum()
    # Also include scaling factors for one-sided densities and dividing by the
    # sampling frequency, if desired. Scale everything, except the DC component
    # and the NFFT/2 component:
    Pxy[1:-1] *= scaling_factor
    # MATLAB divides by the sampling frequency so that density function
    # has units of dB/Hz and can be integrated by the plotted frequency
    # values. Perform the same scaling here.
    if scale_by_freq:
        Pxy /= Fs
    t = 1./Fs * (ind + NFFT / 2.)
    freqs = float(Fs) / pad_to * np.arange(numFreqs)
    if (np.iscomplexobj(x) and sides == 'default') or sides == 'twosided':
        # center the frequency range at zero
        freqs = np.concatenate((freqs[numFreqs//2:] - Fs, freqs[:numFreqs//2]))
        Pxy = np.concatenate((Pxy[numFreqs//2:, :], Pxy[:numFreqs//2, :]), 0)
    return Pxy, freqs, t
