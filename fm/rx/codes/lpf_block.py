from gnuradio import gr, blocks
import numpy as np
import scipy.signal as signal

class LowPassFilter(gr.sync_block):
    """A simple low-pass filter"""

    def __init__(self, sample_rate=2.4e6, cutoff_freq=100e3, order=6, gain=5):
        gr.sync_block.__init__(self,
            name="Low Pass Filter",
            in_sig=[np.complex64],
            out_sig=[np.complex64])

        self.sample_rate = sample_rate
        self.cutoff_freq = cutoff_freq
        self.order = order
        self.gain=gain
        self.zf = np.zeros(self.order)

        # Design the filter kernel using a Hamming window
        nyquist_freq = self.sample_rate / 2
        taps = self.order + 1
        fc_norm = self.cutoff_freq / nyquist_freq
        b = signal.firwin(taps, fc_norm, window='hamming')

        # Scale the filter kernel so that its frequency response has a maximum gain of 1
        b /= self.gain*np.sum(b)

        # Save the filter kernel as a class attribute
        self.filter_kernel = b

    def work(self, input_items, output_items):
        in_buf = input_items[0]
        N = len(in_buf)

        # Apply the filter
        output_items[0][:N], self.zf = signal.lfilter(self.filter_kernel, 1, in_buf, zi=self.zf)

        # Save the last order samples of the input buffer for next time
        self.zf = self.zf[-self.order:]

        return N
