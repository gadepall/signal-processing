import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Configure RTL-SDR parameters
center_freq = 102e6  # Set your desired frequency in Hz
sample_rate = 2.4e6  # Set the sample rate in Hz
gain = 'auto'       # Set the gain ('auto' for automatic gain)

# Create an instance of the RTL-SDR device
sdr = RtlSdr()

# Configure RTL-SDR settings
sdr.center_freq = center_freq
sdr.sample_rate = sample_rate
sdr.gain = gain

# Read samples from the RTL-SDR
num_samples = 1024  # Set the number of samples to read
samples = sdr.read_samples(num_samples)

# Save samples to an output file
output_file = 'samples.iq'
samples.astype(np.complex64).tofile(output_file)

# Plot the samples
plt.figure()
plt.plot(np.real(samples), label='Real')
plt.plot(np.imag(samples), label='Imaginary')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('RTL-SDR Samples raw data')
plt.grid(True)

#plt.savefig('/home/chinni/rtlsdr_pjt/iqsamples2.png')

# Compute the frequency spectrum using FFT
raw_data_spectrum = np.fft.fftshift(np.fft.fft(samples))


# Compute the frequency axis
n = len(samples)
dt = 1 / sdr.sample_rate
freq = np.fft.fftshift(np.fft.fftfreq(n, dt))

# Plot the frequency-domain signals
plt.figure()
plt.plot(freq, np.abs(raw_data_spectrum), label='Raw Data')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Raw Data (Frequency Domain)')
plt.grid(True)
plt.show()
# Close the RTL-SDR device
sdr.close()

