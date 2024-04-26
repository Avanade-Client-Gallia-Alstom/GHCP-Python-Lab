#Generate a code using scipy library to apply FIR on given signal and display both th esignal on map

import numpy as np
from scipy import signal

import matplotlib.pyplot as plt

# Define the input signal
t = np.linspace(0, 1, 1000)  # Time vector
x = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)  # Input signal

# Define the FIR filter coefficients
numtaps = 30  # Number of filter taps
cutoff = 6  # Cutoff frequency
nyquist = 0.5 * 1000  # Nyquist frequency
taps = signal.firwin(numtaps, cutoff / nyquist)

# Apply the FIR filter to the input signal
filtered_signal = signal.lfilter(taps, 1.0, x)

# Plot the original and filtered signals
plt.figure()
plt.plot(t, x, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()