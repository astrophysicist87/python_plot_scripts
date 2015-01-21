#!/usr/bin/env python
from numpy import *
from pylab import *
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def plot_EbE_R2s():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -0.5, 13.5
	
	#load data for R2s, different ens. avgs.
	
	ebs000data=loadtxt('complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')
	ebs008data=loadtxt('complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')
	ebs020data=loadtxt('complete_FOsurface_properties_etaBYs_0.20_1000evs.dat')
	
	#plot data
	ax.plot(ebs000data[:,0],ebs000data[:,1], color='red', linestyle='solid', linewidth=2, label='$\langle R^2_s\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],ebs008data[:,1], color='blue', linestyle='solid', linewidth=2, label='$\langle R^2_s\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],ebs020data[:,1], color='green', linestyle='solid', linewidth=2, label='$\langle R^2_s\\rangle$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],ebs000data[:,1]+sqrt(ebs000data[:,11]), color='red', linestyle='--', linewidth=1, label='$\langle R^2_s\\rangle \pm \sigma_s$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],ebs008data[:,1]+sqrt(ebs008data[:,11]), color='blue', linestyle='--', linewidth=1, label='$\langle R^2_s\\rangle \pm \sigma_s$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],ebs020data[:,1]+sqrt(ebs020data[:,11]), color='green', linestyle='--', linewidth=1, label='$\langle R^2_s\\rangle \pm \sigma_s$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],ebs000data[:,1]-sqrt(ebs000data[:,11]), color='red', linestyle='--', linewidth=1)
	ax.plot(ebs008data[:,0],ebs008data[:,1]-sqrt(ebs008data[:,11]), color='blue', linestyle='--', linewidth=1)
	ax.plot(ebs020data[:,0],ebs020data[:,1]-sqrt(ebs020data[:,11]), color='green', linestyle='--', linewidth=1)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=3,ncol=2,prop={'size': plotfontsize-3})
	
	#plt.savefig('R2s_ens_avg_pm_sig_vs_ebs.pdf', format='pdf')
	plt.show()




def plot_EbE_R2o():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 4.5, 35.0
	
	#load data for R2s, different ens. avgs.
	
	ebs000data=loadtxt('complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')
	ebs008data=loadtxt('complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')
	ebs020data=loadtxt('complete_FOsurface_properties_etaBYs_0.20_1000evs.dat')
	
	#plot data
	ax.plot(ebs000data[:,0],ebs000data[:,2], color='red', linestyle='solid', linewidth=2, label='$\langle R^2_o\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],ebs008data[:,2], color='blue', linestyle='solid', linewidth=2, label='$\langle R^2_o\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],ebs020data[:,2], color='green', linestyle='solid', linewidth=2, label='$\langle R^2_o\\rangle$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],ebs000data[:,2]+sqrt(ebs000data[:,12]), color='red', linestyle='--', linewidth=1, label='$\langle R^2_o\\rangle \pm \sigma_o$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],ebs008data[:,2]+sqrt(ebs008data[:,12]), color='blue', linestyle='--', linewidth=1, label='$\langle R^2_o\\rangle \pm \sigma_o$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],ebs020data[:,2]+sqrt(ebs020data[:,12]), color='green', linestyle='--', linewidth=1, label='$\langle R^2_o\\rangle \pm \sigma_o$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],ebs000data[:,2]-sqrt(ebs000data[:,12]), color='red', linestyle='--', linewidth=1)
	ax.plot(ebs008data[:,0],ebs008data[:,2]-sqrt(ebs008data[:,12]), color='blue', linestyle='--', linewidth=1)
	ax.plot(ebs020data[:,0],ebs020data[:,2]-sqrt(ebs020data[:,12]), color='green', linestyle='--', linewidth=1)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_o$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=1,ncol=1,prop={'size': plotfontsize-3})
	
	#plt.savefig('R2o_ens_avg_pm_sig_vs_ebs.pdf', format='pdf')
	plt.show()














if __name__ == "__main__":
	plot_EbE_R2s()
	plot_EbE_R2o()


# End of file
