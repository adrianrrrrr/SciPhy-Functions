# -*- coding: utf-8 -*-
"""
@company: Amate Audio
@author: Adrián Ramos González
"""

from scipy.signal import chirp, spectrogram
from scipy.io.wavfile import write

import matplotlib.pyplot as plt
import numpy as np
import wave
import struct


# GENERATION OF SWEEP TEST SIGNAL
sampling_rate = 48000
amplitude = 32000 #"Python requeriment" for writting .wav, not de signal ampl.
rep_time = 3 #Representation
num_samples = int(sampling_rate * rep_time) #Samples of the signal + representation


t = [t/sampling_rate for t in range(rep_time*sampling_rate)]

sweep = chirp(t, f0=20, f1=20000, t1=rep_time, method='linear')
plt.plot(t, sweep)

plt.title("Linear Chirp, f(0)=6, f(10)=1")

plt.xlabel('t (sec)')

plt.show()
print("1")

# OUTPUT the SIGNAL IN A WAVE CONTAINER FILE 
file = "sweep_3seconds.wav"
nframes=num_samples 
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2 #Means 2 Bytes = 16 bits
print("2")

wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# struct.pack(format,value) simply returns value in format. Format h is short
# s*amplitude for adjusting to short format. Like a requeriment. 
# https://docs.python.org/3/library/struct.html
counter = 3;
for s in sweep:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
   counter = counter + 1
   
wav_file.close()