'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Number of samples used to compute FFT

import numpy as np
from scipy.io import wavfile

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")
no_of_samples=len(audio_data)
print("The number of samples are:",no_of_samples)
