import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat 5_3.cir | ngspice')
A = np.loadtxt('resp_butter.txt')
n = 5
fc = 60
b, a = signal.butter(n, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)))
plt.grid()
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/5_3.png')
os.system('sh gopen.sh ../figs/5_3.png')
