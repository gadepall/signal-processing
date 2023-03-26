import numpy as np
from matplotlib import pyplot as plt
import os

A = 12
f = 50
t = np.linspace(0, 2/f, 1000)
plt.plot(t, np.abs(A*np.sin(2*np.pi*f*t)))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('../figs/1_1.png')
os.system('sh gopen.sh ../figs/1_1.png')
