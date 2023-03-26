import numpy as np
from matplotlib import pyplot as plt
import os

A = 12
f = 50
N = 1000
t = np.linspace(0, 4/f, N)
B = np.ones(N)*2*A/np.pi

def acc_cos(k):
    global B
    acc = 4*A*np.cos(2*np.pi*f*k*t)/(np.pi*(1 - k**2))
    B += acc

acc_vec = np.vectorize(acc_cos, otypes=['double'])
K = np.linspace(2, 100, 50)
acc_vec(K)
plt.plot(t, np.abs(A*np.sin(2*np.pi*f*t)))
plt.plot(t, B, '.')
plt.legend(['Analysis', 'Simulation'])
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('../figs/2_6.png')
os.system('sh gopen.sh ../figs/2_6.png')
