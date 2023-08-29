import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, hamming

fc1 = 500
fs1 = 6000
wc1 = 2 * np.pi * fc1 / fs1
#print(wc1)
fc2 = 1200
wc2 = 2 * np.pi * fc2 / fs1
#print(wc2)
N = 39
alpha = (N - 1) / 2
n = np.arange(0, N)
#print(n)
hd = (np.sin(wc2*(n-alpha))-np.sin(wc1 * (n - alpha)))/(np.pi * (n - alpha))
hd[int(alpha)] = (wc2 - wc1) / np.pi
#print(hd)

wr = hamming(N)  # Hamming window
# wr = np.hanning(N)  # Hann window
# wr = np.bartlett(N)  # Bartlett window
hn=hd*wr
#hn = hd * wr.T

w = np.arange(0, np.pi + 0.01, 0.01)
w, Hz = freqz(hn,1,w)
#w, Hz = freqz(hn,w)
#print(Hz)
plt.figure()
plt.plot(w / np.pi, np.abs(Hz))
plt.title('Magnitude Response')
plt.xlabel('Normalized Frequency (π radians/sample)')
plt.ylabel('Magnitude')
plt.grid()
plt.savefig('bmagnitude_response.png')
plt.plot(w, np.angle(Hz))
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Phase (radians)')
plt.title('Phase Response')
plt.grid(True)
plt.savefig('bphase_response.png')
plt.show()

