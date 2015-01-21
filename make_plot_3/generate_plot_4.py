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
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 1.07, 1.15
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1,11]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1,11]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1,11]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1,11]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], 1.+sqrt(NEWTDEPV1data[:,2])/NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], 1.+sqrt(NEWTDEPV2data[:,2])/NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], 1.+sqrt(NEWTDEPV3data[:,2])/NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], 1.+sqrt(NEWTDEPV4data[:,2])/NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'1+$\sigma_s / \langle R^2_s\rangle$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=2)
	
	#plt.savefig('R2sDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()
	#plt.savefig('R2s_rel_sig_vs_TDEPVX_w_inset.pdf', format='pdf')


def plot_R2o_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 1.05, 1.2
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2,12]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2,12]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2,12]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2,12]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], 1.+sqrt(NEWTDEPV1data[:,2])/NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], 1.+sqrt(NEWTDEPV2data[:,2])/NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], 1.+sqrt(NEWTDEPV3data[:,2])/NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], 1.+sqrt(NEWTDEPV4data[:,2])/NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'1+$\sigma_o / \langle R^2_o\rangle$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=4)
	
	#plt.savefig('R2oDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()
	#plt.savefig('R2o_rel_sig_vs_TDEPVX_w_inset.pdf', format='pdf')



def plot_R2l_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 1.07, 1.13
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3,13]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3,13]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3,13]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3,13]]
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], 1.+sqrt(NEWTDEPV1data[:,2])/NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], 1.+sqrt(NEWTDEPV2data[:,2])/NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], 1.+sqrt(NEWTDEPV3data[:,2])/NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], 1.+sqrt(NEWTDEPV4data[:,2])/NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')

	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'1+$\sigma_l / \langle R^2_l\rangle$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=2)
	
	#plt.savefig('R2lDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()
	#plt.savefig('R2l_rel_sig_vs_TDEPVX_w_inset.pdf', format='pdf')



def plot_R2ol_TDEP_comparisons():
	
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	# set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 1.07, 1.14
	
	# load data for R2s, different ens. avgs.
	NEWTDEPV1data=loadtxt('NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4,14]]
	NEWTDEPV2data=loadtxt('NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4,14]]
	NEWTDEPV3data=loadtxt('NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4,14]]
	NEWTDEPV4data=loadtxt('NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4,14]]
	
	onezero=zeros(len(NEWTDEPV1data[:,0]))+1
	onezero[0]=0.
	
	# plot data
	ax.plot(NEWTDEPV1data[:,0], 1.-onezero*sqrt(NEWTDEPV1data[:,2])/NEWTDEPV1data[:,1], color='red', linestyle='solid', linewidth=2, label='LH-LQ')
	ax.plot(NEWTDEPV2data[:,0], 1.-onezero*sqrt(NEWTDEPV2data[:,2])/NEWTDEPV2data[:,1], color='blue', linestyle=':', linewidth=2, label='LH-HQ')
	ax.plot(NEWTDEPV3data[:,0], 1.-onezero*sqrt(NEWTDEPV3data[:,2])/NEWTDEPV3data[:,1], color='black', linestyle='-.', linewidth=2, label='HH-LQ')
	ax.plot(NEWTDEPV4data[:,0], 1.-onezero*sqrt(NEWTDEPV4data[:,2])/NEWTDEPV4data[:,1], color='darkgreen', linestyle='--', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'1-$\sigma_{ol} / \langle R^2_{ol}\rangle$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax.legend(loc=4)
	
	#plt.savefig('R2olDEA_vs_TDEPVX_w_inset.pdf', format='pdf')
	plt.show()
	#plt.savefig('R2ol_rel_sig_vs_TDEPVX_w_inset.pdf', format='pdf')





if __name__ == "__main__":
	plot_R2s_TDEP_comparisons()
	plot_R2o_TDEP_comparisons()
	plot_R2l_TDEP_comparisons()
	plot_R2ol_TDEP_comparisons()





# End of file
