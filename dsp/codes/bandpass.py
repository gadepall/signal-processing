import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, hamming

fc1 = 500
fs1 = 6000
wc1 = 2 * np.pi * fc1 / fs1
fc2 = 1200
wc2 = 2 * np.pi * fc2 / fs1

N = 39
alpha = (N - 1) / 2
n = np.arange(0, N)

# Calculate hd using a different approach
hd = np.empty_like(n, dtype=np.float64)
for i, val in enumerate(n):
    if val == alpha:
        hd[i] = (wc2 - wc1) / np.pi
    else:
        hd[i] = (np.sin(wc2 * (val - alpha)) - np.sin(wc1 * (val - alpha))) / (np.pi * (val - alpha))
#print(hd)
wr = hamming(N)
#print(wr)
hn = hd * wr
w = np.arange(0, np.pi + 0.01, 0.01)
w, Hz = freqz(hn, 1, worN=8000)
#print(Hz)
# Create a new figure for magnitude and phase responses
plt.figure(figsize=(10, 6))

# Plot magnitude response
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(Hz))
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Magnitude')
plt.title('Magnitude Response')
plt.grid(True)
plt.savefig('bmagnitude_response.png')
# Plot phase response
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(Hz))
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Phase (radians)')
plt.title('Phase Response')
plt.grid(True)
plt.savefig('bphase_response.png')
plt.tight_layout()
plt.show()
