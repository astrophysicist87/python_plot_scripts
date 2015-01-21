#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#set-up
plotfontsize = 18
transparency = 0.1
colors = ['red', 'blue', 'green']
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

#set axes limits
xlower, xupper = 0.0, 6.5
vTlower, vTupper = 0.0, 0.675

#load data
dataetas000=loadtxt('INTERP_avgANDwidths_etaBYs_0.00_X_gt_0.dat')
dataetas008=loadtxt('INTERP_avgANDwidths_etaBYs_0.08_X_gt_0.dat')
dataetas020=loadtxt('INTERP_avgANDwidths_etaBYs_0.20_X_gt_0.dat')
SEdataetas000=loadtxt('vT_vs_X_etaBYs_0.00.out')
SEdataetas008=loadtxt('vT_vs_X_etaBYs_0.08.out')
SEdataetas020=loadtxt('vT_vs_X_etaBYs_0.20.out')

#plot data
ax1.plot(dataetas000[:,0], dataetas000[:,1], color=colors[0], linestyle='solid', linewidth=2, label='$\eta/s = 0.00$')
ax1.plot(dataetas000[:,0], dataetas000[:,2], color=colors[0], linestyle='solid', linewidth=1)
ax1.plot(dataetas000[:,0], dataetas000[:,3], color=colors[0], linestyle='solid', linewidth=1)
ax1.fill_between(dataetas000[:,0], dataetas000[:,2], dataetas000[:,3], facecolor=colors[0], alpha=transparency)

ax1.plot(dataetas008[:,0], dataetas008[:,1], color=colors[1], linestyle='solid', linewidth=2, label='$\eta/s = 0.08$')
ax1.plot(dataetas008[:,0], dataetas008[:,2], color=colors[1], linestyle='solid', linewidth=1)
ax1.plot(dataetas008[:,0], dataetas008[:,3], color=colors[1], linestyle='solid', linewidth=1)
ax1.fill_between(dataetas008[:,0], dataetas008[:,2], dataetas008[:,3], facecolor=colors[1], alpha=transparency)

ax1.plot(dataetas020[:,0], dataetas020[:,1], color=colors[2], linestyle='solid', linewidth=2, label='$\eta/s = 0.20$')
ax1.plot(dataetas020[:,0], dataetas020[:,2], color=colors[2], linestyle='solid', linewidth=1)
ax1.plot(dataetas020[:,0], dataetas020[:,3], color=colors[2], linestyle='solid', linewidth=1)
ax1.fill_between(dataetas020[:,0], dataetas020[:,2], dataetas020[:,3], facecolor=colors[2], alpha=transparency)

ax1.plot(SEdataetas000[:,1], SEdataetas000[:,0], color=colors[0], linestyle='dashed', linewidth=2)
ax1.plot(SEdataetas008[:,1], SEdataetas008[:,0], color=colors[1], linestyle='dashed', linewidth=2)
ax1.plot(SEdataetas020[:,1], SEdataetas020[:,0], color=colors[2], linestyle='dashed', linewidth=2)

#update axes limits and axes labels
ax1.axis([xlower, xupper, vTlower, vTupper])
ax1.set_xlabel(r'x (fm)', {'fontsize': plotfontsize + 5})
ax1.set_ylabel(r'$v_T$', {'fontsize': plotfontsize + 5})

ax1.legend(loc=2,prop={'size': plotfontsize})

plt.savefig('SE_transverse_flow_profile_vs_etaBYs_w_inset_legend.pdf', format='pdf')
#plt.show()
