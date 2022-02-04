# -*- coding: utf-8 -*-
"""
@company: Amate Audio
@author: Adrián Ramos González
"""

import numpy as np
import wave
import struct

# GENERATION OF SINE TEST SIGNAL
frequency = 1000
period = 1/frequency
sampling_rate =88200.0
amplitude = 32000 #"Python requeriment" for writting .wav, not de signal ampl.
rep_time = 5 #Representation = Signal TODO: IS NOT SECONDS ¿? ¿?
num_samples = int(sampling_rate * rep_time) #Samples of the signal + representation


sine_wave = [ np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples) ]
print("1")

# OUTPUT the SIGNAL IN A WAVE CONTAINER FILE 
file = "sin_f1kHz_fs44100kHz_60s.wav"
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
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
   print(counter)
   counter = counter + 1
   
wav_file.close()