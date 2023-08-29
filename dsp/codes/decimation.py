import numpy as np
import matplotlib.pyplot as plt

# Signal with frequency F=100
Fs = 1200
dt = 1 / Fs
StopTime = 0.03
t = np.arange(0, StopTime - dt, dt)
N = len(t)

f0 = 100
f1 = 500
f2 = 400
x = 1 * np.sin(2 * np.pi * f0 * t) + 0.5 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)
X = np.fft.fftshift(np.fft.fft(x))
dF = Fs / N
f = np.arange(-Fs / 2, Fs / 2, dF)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Input Signal')
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(X) / N)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('d_input.png')
# Filter
h = np.array([-0.0013, 0.0000, 0.0020, -0.0000, -0.0038, 0.0000, 0.0071, -0.0000, -0.0124, 0.0000, 0.0204, -0.0000, -0.0330, 0.0000, 0.0542, -0.0000, -0.1002, 0.0000, 0.3163, 0.5000, 0.3163, 0.0000, -0.1002, -0.0000, 0.0542, 0.0000, -0.0330, -0.0000, 0.0204, 0.0000, -0.0124, -0.0000, 0.0071, 0.0000, -0.0038, -0.0000, 0.0020, 0.0000, -0.0013])

# Output
y11 = np.convolve(x, h)
l1 = (len(h) - 1) // 2
y1 = y11[l1:len(y11) - l1]
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(y1)
plt.title('Output Signal of LPF')
Y1 = np.fft.fftshift(np.fft.fft(y1))
N_out1 = N
dF = Fs / N_out1
f = np.arange(-Fs / 2, Fs / 2, dF)
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(Y1) / N_out1)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('d_l_out.png') 
# Downsample
Fs_deci = Fs / 2
y = y1[::2]
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(y)
plt.title('Output Signal of decimator')
Y = np.fft.fftshift(np.fft.fft(y))
N_out2 = len(y)
dF = Fs_deci / N_out2
f = np.arange(-Fs_deci / 2, Fs_deci / 2, dF)
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(Y) / N_out2)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('output_decimator.png')
# Downsampler without LPF
Fs_deci = Fs / 2
x_d = x[::2]
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x_d)
plt.title('Output Signal of downsampler without LPF')
X_d = np.fft.fftshift(np.fft.fft(x_d))
N_out2 = len(x_d)
dF = Fs_deci / N_out2
f = np.arange(-Fs_deci / 2, Fs_deci / 2, dF)
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(X_d) / N_out2)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('output_downsampler.png')
plt.show()

