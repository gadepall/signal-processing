import numpy as np
from matplotlib import pyplot as plt
import os

N = 100000
s = np.linspace(0, 10000000, N)
R1 = 1
R2 = 2
C = 1e-6
H = R1/(R1+R2+s*C*R1*R2)
plt.plot(s,H)
plt.grid()
plt.xlabel('s')
plt.ylabel('H(s)')
plt.savefig('../figs/4_3.png')
os.system('sh gopen.sh ../figs/4_3.png')
