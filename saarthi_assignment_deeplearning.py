import argparse
import warnings
import IPython
from scipy.io import wavfile
import numpy as np
import io
from scipy.io import wavfile
import soundfile as sf
from scipy import signal
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser(description='Please provide following arguments to proceed')
# Read Arguments from commandline
parser.add_argument("-i", "--input", type=str, required=True, help="Input: Provide input .flac file")
parser.add_argument("-o", "--output", type=str, required=True, help="Input: Provide input .flac file")
# Parameter initialization
args = parser.parse_args()
file=args.input
out=args.output
f=file.split(".")
if f[1]=='wav':
  frequency, sound = wavfile.read(file)
else:
  f1=f[0]+'.wav'
  sound, frequency = sf.read(file)
  sf.write(f1, sound, frequency)
  frequency, sound = wavfile.read(f1)
# IPython.display.Audio(data=sound, rate=frequency)
a,b = signal.butter(5, 1000/(frequency/2), btype='highpass')
sig_fil = signal.lfilter(a,b,sound)
c,d = signal.butter(5, 380/(frequency/2), btype='lowpass')
new_audio= signal.lfilter(c,d,sig_fil)
wavfile.write(out, frequency, new_audio)