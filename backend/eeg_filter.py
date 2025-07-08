import numpy as np
from scipy.signal import iirnotch, butter, filtfilt

def notch_filter(x, fs, freqs=(50,60), q=30):
    y = x.copy()
    for f in freqs:
        b,a = iirnotch(f/(fs/2), q)
        y = filtfilt(b,a,y,axis=-1)
    return y

def band_pass(x, fs, lo=0.5, hi=45, order=4):
    b,a = butter(order, [lo/(fs/2), hi/(fs/2)], btype='band')
    return filtfilt(b,a,x,axis=-1)

def artefact_mask(x, thresh=4):
    z = (x - x.mean(axis=-1, keepdims=True))/x.std(axis=-1, keepdims=True)
    return np.all(np.abs(z) < thresh, axis=0)
