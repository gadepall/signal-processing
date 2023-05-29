
'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Getting the sampling rate of an audio file

#Getting the sampling rate of an audio file
import numpy as np
from scipy.io import wavfile

sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")
print("Sample_rate:",sample_rate)

print(sample_rate)

