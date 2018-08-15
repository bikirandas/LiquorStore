from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt
import xray
def butter_bandpass(lowcut, highcut, fs, order=2):
        n = 0.5 * fs
        low = lowcut / n
        high = highcut / n
        b, a = butter(order, [low, high], btype='bandpass')
        return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
        b, a = butter_bandpass(lowcut, highcut, fs, order=2)
        y = lfilter(b, a, data)
        return y

fs =10*10**3
lowcut = 11.8
highcut = 12.5
dset=xray.open_dataset('temp_6_20dec.nc')
data= dset['TEMP1']
datax= data[:,2,0,0]
y = butter_bandpass_filter(datax, lowcut, highcut, fs, order=2)
fig,ax=plt.subplots()
ax.plot(range(len(datax)),y,'r')
ax1=ax.twinx()
ax1.plot(range(len(datax)),datax,'b')
plt.savefig('filter.png')
plt.show()

