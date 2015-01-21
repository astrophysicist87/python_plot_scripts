#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def relf(a,b):			# returns the percent difference between vectors a and b, element-wise
	#return 200.*(a-b)/(a+b)
	return 100.*(a-b)/b

#set-up
plotfontsize = 18
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig.add_axes([0.2, 0.55, 0.325, 0.325])

#set axes limits
xlower, xupper = 0.0, 6.5
vTlower, vTupper = 0.0, 0.675
pclower, pcupper = -2, 30

#load data
dataetas000=loadtxt('INTERP_avgANDsmooth_etaBYs_0.00_X_gt_0.dat')
dataetas008=loadtxt('INTERP_avgANDsmooth_etaBYs_0.08_X_gt_0.dat')
dataetas020=loadtxt('INTERP_avgANDsmooth_etaBYs_0.20_X_gt_0.dat')

#plot data
ax1.plot(dataetas000[:,0],dataetas000[:,1], color='red', linestyle='solid', linewidth=2, label='$\eta/s = 0.00$')
ax1.plot(dataetas000[:,0],dataetas000[:,2], color='red', linestyle='dashed', linewidth=2)
#ax2.plot(dataetas000[:,0],dataetas000[:,3], color='red', linewidth=2)
ax2.plot(dataetas000[:,0],relf(dataetas000[:,1],dataetas000[:,2]), color='red', linewidth=2)

ax1.plot(dataetas008[:,0],dataetas008[:,1], color='blue', linestyle='solid', linewidth=2, label='$\eta/s = 0.08$')
ax1.plot(dataetas008[:,0],dataetas008[:,2], color='blue', linestyle='dashed', linewidth=2)
#ax2.plot(dataetas008[:,0],dataetas008[:,3], color='blue', linewidth=2)
ax2.plot(dataetas020[:,0],relf(dataetas008[:,1],dataetas008[:,2]), color='blue', linewidth=2)

ax1.plot(dataetas020[:,0],dataetas020[:,1], color='green', linestyle='solid', linewidth=2, label='$\eta/s = 0.20$')
ax1.plot(dataetas020[:,0],dataetas020[:,2], color='green', linestyle='dashed', linewidth=2)
#ax2.plot(dataetas020[:,0],dataetas020[:,3], color='green', linewidth=2)
ax2.plot(dataetas020[:,0],relf(dataetas020[:,1],dataetas020[:,2]), color='green', linewidth=2)

#update axes limits and axes labels
ax1.axis([xlower, xupper, vTlower, vTupper])
ax2.axis([xlower, xupper, pclower, pcupper])
ax1.set_xlabel(r'x (fm)', {'fontsize': plotfontsize + 5})
ax1.set_ylabel(r'$v_T$', {'fontsize': plotfontsize + 5})
ax2.set_xlabel(r'x (fm)', {'fontsize': plotfontsize - 5})
ax2.set_ylabel(r'p.c. deviation', {'fontsize': plotfontsize - 7})

ax1.legend(loc=4,prop={'size': plotfontsize})

#plt.show()
plt.savefig('transverse_flow_profiles_vs_etaBYs_w_inset_legend.pdf', format='pdf')
#plt.savefig('transverse_flow_profiles_vs_etaBYs_w_inset.eps', format='eps')
