#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt

m_pion = 0.13957

def betaT(KT):
	return KT/sqrt(KT**2 + m_pion**2)

def make_plot_1():
	#this function generate relative HBT widths vs. KT for different eta/s, for R2o and R2s
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99, 1.16
	
	#load data for R2s, different ens. avgs.
	
	ebs000data=loadtxt('complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')
	ebs008data=loadtxt('complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')
	ebs020data=loadtxt('complete_FOsurface_properties_etaBYs_0.20_1000evs.dat')
	
	#plot data
	ax.plot(ebs000data[:,0],1+sqrt(ebs000data[:,11])/ebs000data[:,1], color='red', linestyle='--', linewidth=2, label='$1 + \sigma_s/\langle R^2_s\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],1+sqrt(ebs008data[:,11])/ebs008data[:,1], color='blue', linestyle='--', linewidth=2, label='$1 + \sigma_s/\langle R^2_s\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],1+sqrt(ebs020data[:,11])/ebs020data[:,1], color='green', linestyle='--', linewidth=2, label='$1 + \sigma_s/\langle R^2_s\\rangle$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],1+sqrt(ebs000data[:,12])/ebs000data[:,2], color='red', linestyle='-.', linewidth=3, label='$1 + \sigma_o/\langle R^2_o\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],1+sqrt(ebs008data[:,12])/ebs008data[:,2], color='blue', linestyle='-.', linewidth=3, label='$1 + \sigma_o/\langle R^2_o\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],1+sqrt(ebs020data[:,12])/ebs020data[:,2], color='green', linestyle='-.', linewidth=3, label='$1 + \sigma_o/\langle R^2_o\\rangle$, $\eta/s = 0.20$')
	ax.axhline(1.0, color='black', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	#ax.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=(0.025,0.1),ncol=2,prop={'size': plotfontsize-3})
	
	#plt.savefig('R2s_and_R2o_rel_widths_vs_ebs.pdf', format='pdf')
	plt.show()




def make_plot_2():
	#this function generate relative HBT widths vs. KT for different eta/s, for R2o and R2s
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99, 1.12
	
	#load data for R2s, different ens. avgs.
	
	ebs000data=loadtxt('complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')
	ebs008data=loadtxt('complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')
	ebs020data=loadtxt('complete_FOsurface_properties_etaBYs_0.20_1000evs.dat')

	onezero=zeros(len(ebs000data[:,0]))+1
	onezero[0]=0.
	
	#plot data
	ax.plot(ebs000data[:,0],1+sqrt(ebs000data[:,13])/ebs000data[:,3], color='red', linestyle='--', linewidth=2, label='$1 + \sigma_l/\langle R^2_l\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],1+sqrt(ebs008data[:,13])/ebs008data[:,3], color='blue', linestyle='--', linewidth=2, label='$1 + \sigma_l/\langle R^2_l\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],1+sqrt(ebs020data[:,13])/ebs020data[:,3], color='green', linestyle='--', linewidth=2, label='$1 + \sigma_l/\langle R^2_l\\rangle$, $\eta/s = 0.20$')
	ax.plot(ebs000data[:,0],1-onezero*sqrt(ebs000data[:,14])/ebs000data[:,4], color='red', linestyle='-.', linewidth=3, label='$1 + \sigma_{ol}/\langle R^2_{ol}\\rangle$, $\eta/s = 0.00$')
	ax.plot(ebs008data[:,0],1-onezero*sqrt(ebs008data[:,14])/ebs008data[:,4], color='blue', linestyle='-.', linewidth=3, label='$1 + \sigma_{ol}/\langle R^2_{ol}\\rangle$, $\eta/s = 0.08$')
	ax.plot(ebs020data[:,0],1-onezero*sqrt(ebs020data[:,14])/ebs020data[:,4], color='green', linestyle='-.', linewidth=3, label='$1 + \sigma_{ol}/\langle R^2_{ol}\\rangle$, $\eta/s = 0.20$')
	ax.axhline(1.0, color='black', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	#ax.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=(0.025,0.15),ncol=2,prop={'size': plotfontsize-3})
	
	#plt.savefig('R2l_and_R2ol_rel_widths_vs_ebs.pdf', format='pdf')
	plt.show()





def make_plot_3():
	#this function generate relative HBT widths vs. KT for different eta/s, for R2o and R2s
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99, 1.12
	
	#load data for R2s, different ens. avgs.
	
	ebs000data=loadtxt('complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')
	ebs008data=loadtxt('complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')
	ebs020data=loadtxt('complete_FOsurface_properties_etaBYs_0.20_1000evs.dat')

	onezero=zeros(len(ebs000data[:,0]))+1
	onezero[0]=0.
	
	#plot data
	ax.plot(ebs000data[:,0], 1.+sqrt(ebs000data[:,18])/ebs000data[:,2], color='red', linestyle=':', linewidth=3)
	ax.plot(ebs008data[:,0], 1.+sqrt(ebs008data[:,18])/ebs008data[:,2], color='blue', linestyle=':', linewidth=3)
	ax.plot(ebs020data[:,0], 1.+sqrt(ebs020data[:,18])/ebs020data[:,2], color='green', linestyle=':', linewidth=3)
	ax.plot(ebs000data[:,0], 1.+2.*betaT(ebs000data[:,0])*sqrt(ebs000data[:,15])/ebs000data[:,2], color='red', linestyle='-.', linewidth=3)
	ax.plot(ebs008data[:,0], 1.+2.*betaT(ebs008data[:,0])*sqrt(ebs008data[:,15])/ebs008data[:,2], color='blue', linestyle='-.', linewidth=3)
	ax.plot(ebs020data[:,0], 1.+2.*betaT(ebs020data[:,0])*sqrt(ebs020data[:,15])/ebs020data[:,2], color='green', linestyle='-.', linewidth=3)
	ax.plot(ebs000data[:,0], 1.+betaT(ebs000data[:,0])*betaT(ebs000data[:,0])*sqrt(ebs000data[:,20])/ebs000data[:,2], color='red', linestyle='--', linewidth=2)
	ax.plot(ebs008data[:,0], 1.+betaT(ebs008data[:,0])*betaT(ebs008data[:,0])*sqrt(ebs008data[:,20])/ebs008data[:,2], color='blue', linestyle='--', linewidth=2)
	ax.plot(ebs020data[:,0], 1.+betaT(ebs020data[:,0])*betaT(ebs020data[:,0])*sqrt(ebs020data[:,20])/ebs020data[:,2], color='green', linestyle='--', linewidth=2)
	ax.axhline(1.0, color='black', linewidth=2)
	#ax.axhline(-1.0, color='black', linestyle=':', linewidth=3, label='$Z = \langle \~x^2_o \\rangle$')
	#ax.axhline(-1.0, color='black', linestyle='-.', linewidth=3, label='$Z = \langle \~x_o \~t \\rangle$')
	#ax.axhline(-1.0, color='black', linestyle='--', linewidth=2, label='$Z = \langle \~t ^2 \\rangle$')
	ax.axhline(-1.0, color='black', linestyle=':', linewidth=3, label='$Z = \langle \~x^2_o \\rangle$')
	ax.axhline(-1.0, color='black', linestyle='-.', linewidth=3, label='$Z = 2 \\beta_{\perp} \langle \~x_o \~t \\rangle$')
	ax.axhline(-1.0, color='black', linestyle='--', linewidth=2, label='$Z = \\beta^2_{\perp} \langle \~t ^2 \\rangle$')
	ax.axhline(-1.0, color='red', linestyle='solid', linewidth=2, label='$\eta/s = 0.00$')
	ax.axhline(-1.0, color='blue', linestyle='solid', linewidth=2, label='$\eta/s = 0.08$')
	ax.axhline(-1.0, color='green', linestyle='solid', linewidth=2, label='$\eta/s = 0.20$')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	#ax.set_ylabel(r'$1 + |\sigma(Z)|/\langle R^2_o\\rangle$)', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc='best',ncol=2,prop={'size': plotfontsize-3})
	
	plt.savefig('SV_in_R2o_rel_widths_vs_ebs.pdf', format='pdf')
	#plt.show()







if __name__ == "__main__":
	#make_plot_1()
	#make_plot_2()
	make_plot_3()


# End of file
