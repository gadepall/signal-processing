import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

class LowPassFilter:
    """A simple low-pass filter"""

    def __init__(self, sample_rate=2.4e6, cutoff_freq=100e3, order=6, gain=5):
        self.sample_rate = sample_rate
        self.cutoff_freq = cutoff_freq
        self.order = order
        self.gain = gain
        self.zf = np.zeros(self.order)

        # Design the filter kernel using a Hamming window
        nyquist_freq = self.sample_rate / 2
        taps = self.order + 1
        fc_norm = self.cutoff_freq / nyquist_freq
        b = signal.firwin(taps, fc_norm, window='hamming')

        # Scale the filter kernel so that its frequency response has a maximum gain of 1
        b /= self.gain * np.sum(b)

        # Save the filter kernel as a class attribute
        self.filter_kernel = b

    def filter(self, input_signal):
        # Apply the filter
        output_signal, self.zf = signal.lfilter(self.filter_kernel, 1, input_signal, zi=self.zf)

        # Save the last order samples of the input buffer for next time
        self.zf = self.zf[-self.order:]

        return output_signal

# Read the complex IQ data from the .iq file
filename = 'output.iq'  # Replace with your .iq file path
iq_data = np.fromfile(filename, dtype=np.complex64)

#real_data = np.real(iq_data)
#imag_data = np.imag(iq_data)

plt.figure()
plt.plot(np.real(iq_data), label='Real')
plt.plot(np.imag(iq_data), label='Imaginary')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('raw_data')
plt.legend()
plt.grid(True)


# Create an instance of the LowPassFilter
lpf = LowPassFilter()

# Apply the filter to the IQ data
filtered_data = lpf.filter(iq_data)

# Plot the real and imaginary parts of the filtered data
plt.figure()
plt.plot(np.real(filtered_data), label='Real')
plt.plot(np.imag(filtered_data), label='Imaginary')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('filtered_data')
plt.legend()
plt.grid(True)


# Compute the frequency spectrum using FFT
raw_data_spectrum = np.fft.fftshift(np.fft.fft(iq_data))
filtered_data_spectrum = np.fft.fftshift(np.fft.fft(filtered_data))

# Compute the frequency axis
n = len(iq_data)
dt = 1 / lpf.sample_rate
freq = np.fft.fftshift(np.fft.fftfreq(n, dt))

# Plot the frequency-domain signals
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(freq, np.abs(raw_data_spectrum), label='Raw Data')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Raw Data (Frequency Domain)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(filtered_data_spectrum), label='Filtered Data')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Filtered Data (Frequency Domain)')
plt.grid(True)

plt.tight_layout()
plt.show()









