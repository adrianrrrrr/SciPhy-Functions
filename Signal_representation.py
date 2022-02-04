# -*- coding: utf-8 -*-
"""
@company: Amate Audio
@author: Adrián Ramos González
"""

import wave
import struct
import matplotlib.pyplot as plt
import math


# LOADING THE TEST SIGNAL
infile = "X14FD FLAT HF.wav"	
wav_file = wave.open(infile, 'r')
sampwidth = wav_file.getsampwidth() #Bytes
sampwidth_bits = sampwidth * 8 #Bits
frame_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()

data = wav_file.readframes(num_samples)
wav_file.close()

# "Unpacking" from file. Meaning going from binary to float
#
wav_scale_factor = 2 ** (sampwidth_bits - 1)
data = struct.unpack('{n}h'.format(n=num_samples), data)
data = [x/wav_scale_factor for x in data]

# Generating the time vector
t = [t/frame_rate for t in range(num_samples)]

# SIMPLE PLOTTING OF A SIGNAL. LIKE MATLAB PLOT() FUNCTION 
fig, ax = plt.subplots()
ax.plot(t,data)

ax.set(xlabel='time (s)', ylabel='Normalized amplitude',
       title='Time Signal Representation')
ax.grid()
#fig.savefig("test.png") - For saving the figure
plt.show()

# Output key info
first_peak_index = data.index(max(data))
delay = first_peak_index/frame_rate #seconds
delay = delay*1000 #miliseconds
#truncate number
factor = 10.0 ** 2
delay_tr = math.trunc(delay * factor) / factor

print(f'Delay: {delay_tr} ms | {first_peak_index} samples')

