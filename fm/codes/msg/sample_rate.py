import numpy as np
from scipy.io import wavfile

sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")
print(sample_rate)

