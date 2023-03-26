import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('ngspice 1_7.cir')
T = 1e-7
R = 2
V = 2
C = 1e-6
tau = R*C
k = 1/tau
p = (2*tau-T)/(2*tau+T)
t = np.linspace(0, 1e-5, 101)
n = np.arange(0, 101, 1)
vn = 1 - p**n
vn = np.pad(vn, (0,1), constant_values=(0,0)) + np.pad(vn, (1,0), constant_values=(0,0))
vn[0] = 0
plt.plot(t, V*(1 - np.exp(-k*t)))
plt.plot(t, (V/2)*vn[:len(t)], '.')
v3 = np.loadtxt('v3.txt')
plt.plot(v3[:,0], v3[:,1], '.')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Output (V)')
plt.legend(['Theory (continuous)', 'Theory (discrete)', 'Simulation (ngspice)'])
plt.savefig('../figs/1_7.png')
plt.tight_layout()
os.system('termux-open ../figs/1_7.png')
