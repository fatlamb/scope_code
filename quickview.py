import ROOT
import numpy as np
import matplotlib.pyplot as plt

myfile=ROOT.TFile("ch17_direct.root")


paramtree=myfile.Get("waveforminfo")

for info_ev in paramtree:
	nsamps=info_ev.samples_per_waveform
	samp_time=info_ev.secs_per_sample[1]

print "NS:",nsamps
print "ST:",samp_time

time_array=np.arange(nsamps)
time_array=np.multiply(time_array,samp_time)
	
mytree=myfile.Get("waveformdata")


for event in mytree:

	voltage=np.asarray(event.ch2wfms)
	print voltage
	plt.plot(time_array,voltage)
	plt.show()
