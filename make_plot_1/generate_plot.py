#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def plot_CM2():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 2.0, 5000.0
	ylower, yupper = 0.85, 1.05
	
	exact = 1.
	
	#load data
	CM2data=loadtxt('HBTwidths_sig2.dat')
	exactCM2data=array([exact for i in CM2data[:,0]])
	
	#plot data
	ax.plot(CM2data[:,0],CM2data[:,1], color='red', linestyle='solid', linewidth=2, label="M=100")
	ax.plot(CM2data[:,0],CM2data[:,2], color='blue', linestyle='solid', linewidth=2, label="M=1000")
	ax.plot(CM2data[:,0],CM2data[:,3], color='green', linestyle='solid', linewidth=2, label="M=10000")
	ax.plot(CM2data[:,0], exactCM2data, color='black', linestyle='solid', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$n_b$', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$\sigma^2_{\mathrm{est}} / \sigma^2_{\mathrm{exact}}$', {'fontsize': plotfontsize + 5})
	ax.set_xscale('log')
	
	ax.legend(loc=4,prop={'size': plotfontsize + 5})
	
	plt.savefig('HBTwidths_sig2.pdf', format='pdf')
	#plt.savefig('transverse_flow_profiles_vs_etaBYs_w_inset.eps', format='eps')
	#plt.show()

def plot_CM3():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 2.0, 5000.0
	ylower, yupper = -4.0, 3.5
	
	exact = 1.
	
	#load data
	CM3data=loadtxt('HBTwidths_beta3.dat')
	exactCM3data=array([exact for i in CM3data[:,0]])
	
	#plot data
	ax.plot(CM3data[:,0],CM3data[:,1], color='red', linestyle='solid', linewidth=2, label="M=100")
	ax.plot(CM3data[:,0],CM3data[:,2], color='blue', linestyle='solid', linewidth=2, label="M=1000")
	ax.plot(CM3data[:,0],CM3data[:,3], color='green', linestyle='solid', linewidth=2, label="M=10000")
	ax.plot(CM3data[:,0], exactCM3data, color='black', linestyle='solid', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$n_b$', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$\beta_{3,\mathrm{est}} / \beta_{3,\mathrm{exact}}$', {'fontsize': plotfontsize + 5})
	ax.set_xscale('log')
	#ax.set_yscale('log')
	
	ax.legend(loc=4,prop={'size': plotfontsize + 5})
	
	plt.savefig('HBTwidths_beta3.pdf', format='pdf')
	#plt.savefig('transverse_flow_profiles_vs_etaBYs_w_inset.eps', format='eps')
	#plt.show()

def plot_CM4():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	#set axes limits
	xlower, xupper = 80.0, 5000.0
	ylower, yupper = -6.0, 2.5
	
	exact = 1.
	
	#load data
	CM4data=loadtxt('HBTwidths_beta4m3.dat')
	exactCM4data=array([exact for i in CM4data[:,0]])
	
	#plot data
	ax.plot(CM4data[:,0],CM4data[:,1], color='red', linestyle='solid', linewidth=2, label="M=100")
	ax.plot(CM4data[:,0],CM4data[:,2], color='blue', linestyle='solid', linewidth=2, label="M=1000")
	ax.plot(CM4data[:,0],CM4data[:,3], color='green', linestyle='solid', linewidth=2, label="M=10000")
	ax.plot(CM4data[:,0], exactCM4data, color='black', linestyle='solid', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$n_b$', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$\left(\beta_{4,\mathrm{est}} - 3\right) / \left(\beta_{4,\mathrm{exact}} -3 \right)$', {'fontsize': plotfontsize + 5})
	ax.set_xscale('log')
	#ax.set_yscale('log')
	
	ax.legend(loc=4,prop={'size': plotfontsize + 5})
	
	plt.savefig('HBTwidths_beta4m3.pdf', format='pdf')
	#plt.savefig('transverse_flow_profiles_vs_etaBYs_w_inset.eps', format='eps')
	#plt.show()




if __name__ == "__main__":
	plot_CM2()
	plot_CM3()
	plot_CM4()
