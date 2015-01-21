#!/usr/bin/env python
from numpy import *
from pylab import *
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def relf(a,b):
	return 100.*(a-b)/b

def plot_R2s_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.15, 0.15, 0.3, 0.3])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 13.75
	pclower, pcupper = -10.0, 60.0
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# plot inset
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(NEWTDEPV2data[:,0], relf(NEWTDEPV2data[:,1],NEWTDEPV1data[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(NEWTDEPV3data[:,0], relf(NEWTDEPV3data[:,1],NEWTDEPV1data[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(NEWTDEPV4data[:,0], relf(NEWTDEPV4data[:,1],NEWTDEPV1data[:,1]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend()
	
	#plt.savefig('R2sDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()


def plot_R2o_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.4, 0.5, 0.45, 0.35])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 5.0, 35.0
	pclower, pcupper = -25.0, 25.0
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# plot inset
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(NEWTDEPV2data[:,0], relf(NEWTDEPV2data[:,1],NEWTDEPV1data[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(NEWTDEPV3data[:,0], relf(NEWTDEPV3data[:,1],NEWTDEPV1data[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(NEWTDEPV4data[:,0], relf(NEWTDEPV4data[:,1],NEWTDEPV1data[:,1]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_o$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=3)
	
	#plt.savefig('R2oDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()



def plot_R2l_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.3, 0.3, 0.45, 0.35])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 75.0
	pclower, pcupper = -30.0, 10.0
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# plot inset
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(NEWTDEPV2data[:,0], relf(NEWTDEPV2data[:,1],NEWTDEPV1data[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(NEWTDEPV3data[:,0], relf(NEWTDEPV3data[:,1],NEWTDEPV1data[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(NEWTDEPV4data[:,0], relf(NEWTDEPV4data[:,1],NEWTDEPV1data[:,1]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_l$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend()
	
	#plt.savefig('R2lDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()



def plot_R2ol_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	axinset = fig.add_axes([0.4, 0.4, 0.45, 0.45])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 30.0
	pclower, pcupper = -20.0, 5.0
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], -NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], -NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], -NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], -NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	onezero=zeros(len(NEWTDEPV1data[:,0]))+1
	onezero[0]=0.
	
	# plot inset
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(NEWTDEPV2data[:,0], onezero*relf(-NEWTDEPV2data[:,1],-NEWTDEPV1data[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(NEWTDEPV3data[:,0], onezero*relf(-NEWTDEPV3data[:,1],-NEWTDEPV1data[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(NEWTDEPV4data[:,0], onezero*relf(-NEWTDEPV4data[:,1],-NEWTDEPV1data[:,1]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$-R^2_{ol}$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=3)
	
	#plt.savefig('R2olDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()





if __name__ == "__main__":
	plot_R2s_TDEP_comparisons()
	plot_R2o_TDEP_comparisons()
	plot_R2l_TDEP_comparisons()
	plot_R2ol_TDEP_comparisons()





# End of file
