import numpy as np
from matplotlib import pyplot as plt
import os

f = 50
V = 5
A = 12
N = 100000
fc = 100
tp = 100000
t = np.linspace(-tp, tp, N)
s1 = fc*np.sinc(fc*t)
s2 = A*np.abs(np.sin(2*np.pi*f*t))
sc = np.convolve(s1, s2, mode='same')
plt.plot(t, sc*(np.pi*V/(2*A))*(2*tp/N))
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('V')
plt.savefig('../figs/4_3.png')
os.system('sh gopen.sh ../figs/4_3.png')
