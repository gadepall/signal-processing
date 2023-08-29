import numpy as np
from gnuradio import gr
import scipy.signal as signal

class WBFMDemodulator(gr.sync_block):
    def __init__(self, sample_rate=2.4e6, max_deviation=75e3):
        gr.sync_block.__init__(self,
                               name='WBFMDemodulator',
                               in_sig=[np.complex64],
                               out_sig=[np.float32])

        self.sample_rate = sample_rate
        self.max_deviation = max_deviation
        self._phase = 0

    def work(self, input_items, output_items):
        in_data = input_items
        out_data = output_items

        for i in range(len(in_data)):
            diff_signal = np.diff(in_data[i], prepend=0.0) / (2 * np.pi * sample_rate)
            cutoff_freq = 15e3
            nyquist_rate = self.sample_rate / 2
            b, a = butter(5, cutoff_freq / nyquist_rate)
            filtered_signal = filtfilt(b, a, diff_signal)
            t = np.arange(len(filtered_signal)) / self.sample_rate
            i_signal = filtered_signal * np.cos(2 * np.pi * self.max_deviation * t)
            q_signal = filtered_signal * np.sin(2 * np.pi * self.max_deviation * t)
            fm_signal = i_signal + 1j * q_signal
            magnitude = np.abs(fm_signal)
            phase = np.angle(fm_signal)
            demodulated_signal = np.diff(phase, prepend=0.0) / (2 * np.pi * sample_rate)
            audio_cutoff_freq = 3e3
            audio_b, audio_a = butter(5, audio_cutoff_freq / nyquist_rate)
            audio_signal = filtfilt(audio_b, audio_a, demodulated_signal)
            
            out_data[i] = audio_signal

        return len(out_data)
