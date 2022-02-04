# -*- coding: utf-8 -*-
"""
@company: Amate Audio
@author: Adrián Ramos González

"""

import wave
import struct
import matplotlib.pyplot as plt
import numpy as np

# !!! TODO: REMOVE COMMENT FROM INFILE !!!
# INPUT SIGNAL NAME. CONCATENATE .WAV IF NOT TYPED 
infile = input('Enter the .wav file name\n')

if '.wav' not in infile:
    infile = infile+'.wav'

# Loading the signal into <data> variable
wav_file = wave.open(infile, 'r')

frame_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()
nchannels = wav_file.getnchannels()
sampwidth = wav_file.getsampwidth()
sampwidth_bits = sampwidth * 8

data = wav_file.readframes(num_samples)

wav_file.close()

# Unpacking. Python requeriment 
wav_scale_factor = 2 ** (sampwidth_bits - 1)
data = struct.unpack('{n}h'.format(n=num_samples), data)
data = [x/wav_scale_factor for x in data]

# Generating the time vector for the representations
t = [t/frame_rate for t in range(num_samples)]

# Asking for the delay in ms
delay = input('Enter de delay to apply in miliseconds\n')
delay = float(delay)

# Computing the delay
delay_samples = delay * 0.001 * frame_rate # time(s) * Fs = samples 
delay_samples = round(delay_samples)
delay_samples = int(delay_samples)

# A bit confusing if not used to python indexation but this is the way for
# a signal shift. 
data_delayed = data[-delay_samples:] + data[:-delay_samples]

# Plot  the signals in the same graphic
# Generating the time vector

t = np.arange(0,0.55,1/frame_rate)

# SIMPLE PLOTTING OF A SIGNAL. LIKE MATLAB PLOT() FUNCTION 
fig, ax = plt.subplots()

ax.plot(t,data[:len(t)],t,data_delayed[:len(t)])
ax.set(xlabel='time (s)', ylabel='Normalized amplitude',
       title='Time Signal Representation')
ax.grid()
#fig.savefig("test.png") - For saving the figure
plt.show()

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
