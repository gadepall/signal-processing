import numpy as np
import matplotlib.pyplot as plt

# clear command window, workspace, close figures
# clc
# clear
# close all

# input signal
input = np.array([0.1969, 0.8309, 0.8815, -0.0099, -0.8613, -0.8698, 0.0031, 0.8655, 0.8670, 0.0000, -0.8670, -0.8655, -0.0031, 0.8698, 0.8613, 0.0099, -0.8815, -0.8309])
t = np.arange(1, 2 * len(input) + 1)  # time
t_alt = t[::2]

# upsample
upsampledInput = np.zeros(2 * len(input))
upsampledInput[::2] = input

# hbFilter
hbFilter = np.array([-0.0013, 0.0000, 0.0020, -0.0000, -0.0038, 0.0000, 0.0071, -0.0000, -0.0124, 0.0000, 0.0204, -0.0000, -0.0330, 0.0000, 0.0542, -0.0000, -0.1002, 0.0000, 0.3163, 0.5000, 0.3163, 0.0000, -0.1002, -0.0000, 0.0542, 0.0000, -0.0330, -0.0000, 0.0204, 0.0000, -0.0124, -0.0000, 0.0071, 0.0000, -0.0038, -0.0000, 0.0020, 0.0000, -0.0013])

# hbFilter convolution
y_conv = np.convolve(hbFilter, upsampledInput)

# remove extra samples
l = (len(hbFilter) - 1) // 2
interpolatedOutput = y_conv[l:l + len(upsampledInput)]

# plotting figures
plt.figure()
plt.subplot(3, 1, 1)
plt.stem(t_alt, input, markerfmt='ro', linefmt='r')
plt.title('Input Signal')

plt.subplot(3, 1, 2)
plt.stem(t, upsampledInput, markerfmt='bs', linefmt='b')
plt.title('Upsampled Input Signal')

plt.subplot(3, 1, 3)
plt.stem(t, interpolatedOutput, markerfmt='g^', linefmt='g')
plt.title('Interpolated Output Signal')
plt.grid(True)
plt.savefig('istem_plots.png')


Fs = 1200  # samples per second
dt = 1 / Fs  # seconds per sample
StopTime = 0.03  # seconds
t1 = np.arange(0, len(interpolatedOutput) * dt, dt)
N = len(t1)
X = np.fft.fftshift(np.fft.fft(interpolatedOutput))
dF = Fs / N  # hertz
f = np.arange(-Fs / 2, Fs / 2, dF)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t1, interpolatedOutput)
plt.title('Interpolated Output Signal')
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(X) / N)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('interpolated_output.png')
X_up = np.fft.fftshift(np.fft.fft(upsampledInput))
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t1, upsampledInput)
plt.title('Upsampled Output Signal')
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(X_up) / N)
plt.xlabel('Frequency (in hertz)')
plt.title('Magnitude Response')
plt.savefig('iupsampled_output.png')
plt.show()

