import numpy as np
from matplotlib import pyplot as plt
import os

N = 100000
s = np.linspace(0, 10000000, N)
R = 2
C = 1e-6
H = 1/(1+s*C*R)
plt.plot(s,H)
plt.grid()
plt.xlabel('s')
plt.ylabel('H(s)')
plt.savefig('../figs/1_3.png')
plt.tight_layout()
os.system('termux-open ../figs/1_3.png')
