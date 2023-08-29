import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# LPF with fc = 300 (continuous time cutoff freq)
fc = 300
f = 1200
w = 2 * np.pi * fc / f
N = 39

hd = np.zeros(N)
for k in range(-(N - 1) // 2, (N - 1) // 2 + 1):
    if k == 0:
        hd[k + (N - 1) // 2] = w / np.pi
    else:
        hd[k + (N - 1) // 2] = np.sin(w * k) / (np.pi * k)



#w1 = np.ones(N)
w2 = np.hamming(N)
#w3 = np.hanning(N)
#w4 = np.bartlett(N)

#h1 = hd * w1
h2 = hd * w2
#h3 = hd * w3
#h4 = hd * w4

# Frequency response
w, h = signal.freqz(h2, 1)
plt.figure()
plt.plot(w, 20 * np.log10(abs(h)))
plt.title("Hamming Windowed Low-Pass Filter Frequency Response")
plt.xlabel("Frequency [radians/sample]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.savefig('lpf.png')
plt.show()

