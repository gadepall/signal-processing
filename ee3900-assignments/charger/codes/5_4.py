import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat 5_4.cir | ngspice')
A = np.loadtxt('resp_cheby.txt')
n = 4
fc = 60
rp = 0.5
b, a = signal.cheby1(n, rp, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)))
plt.grid()
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/5_4.png')
os.system('sh gopen.sh ../figs/5_4.png')
