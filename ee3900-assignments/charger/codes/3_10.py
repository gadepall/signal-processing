import numpy as np
from scipy import fft, signal
from matplotlib import pyplot as plt
import os

def rect_smpl(x): return 1 if (np.abs(x) <= 0.5) else 0
rect = np.vectorize(rect_smpl, otypes=['double'])

ts = 2e-4
N = 100
mid = int(N/ts)
sig = np.sinc(np.arange(-N, N, ts))
sig_fft = fft.fftshift(fft.fft(sig))
sig_fft = np.abs(sig_fft)/np.abs(sig_fft[mid])
sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))
plt.plot(sf, sig_fft, '.')
plt.plot(sf, rect(sf))
plt.legend(['Simulation', 'Analysis'])
plt.grid()
plt.xlim(-2, 2)
plt.xlabel('f (Hz)')
plt.ylabel('H(f)')
plt.savefig('../figs/3_10.png')
os.system('sh gopen.sh ../figs/3_10.png')
