# -*- coding: utf-8 -*-
"""
@company: Amate Audio
@author: Adrián Ramos González
"""

import wave
import struct
import math


# LOADING THE SIGNAL
infile = "X102_Flat_LF.wav"	
wav_file = wave.open(infile, 'r')

frame_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()
nchannels = wav_file.getnchannels()
sampwidth = wav_file.getsampwidth()
sampwidth_bits = sampwidth * 8

data = wav_file.readframes(num_samples)

wav_file.close()

# Unpacking
wav_scale_factor = 2 ** (sampwidth_bits - 1)
data = struct.unpack('{n}h'.format(n=num_samples), data)
data = [x/wav_scale_factor for x in data]

# Generating the time vector
t = [t/frame_rate for t in range(num_samples)]

# Computing delay finder
first_peak_index = data.index(max(data))
delay = first_peak_index/frame_rate #seconds
delay_ms = delay*1000 #miliseconds

data_right_side = data[first_peak_index:]
data_left_side = data[:first_peak_index]
data =  data_right_side + data_left_side

# Output key info
#truncate number
factor = 10.0 ** 2
delay_tr = math.trunc(delay_ms * factor) / factor
print(f'Delay: {delay_tr} ms | {first_peak_index} samples')

# OUTPUT the SIGNAL IN A WAVE CONTAINER FILE 
file = infile[:-4]+'_DELAYED.wav'
comptype="NONE"
compname="not compressed"

wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, frame_rate, num_samples, comptype, compname))

# struct.pack(format,value) simply returns value in format. Format h is short
# s*amplitude for adjusting to short format. Like a requeriment. 
# https://docs.python.org/3/library/struct.html
for s in data:
   wav_file.writeframes(struct.pack('h', int(s*wav_scale_factor)))
   
wav_file.close()
