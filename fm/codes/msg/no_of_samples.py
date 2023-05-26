#Number of samples

import numpy as np
from scipy.io import wavfile
import scipy.signal as signal



#Fs, audio_data = wavfile.read("Sound.wav")
#Reading the audio data into the variable audio_data
sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")
no_of_samples=len(audio_data)
print("The number of samples are:",no_of_samples)
