#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def relf(a,b):			# returns the percent difference between vectors a and b, element-wise
	#return 200.*(a-b)/(a+b)
	return 1.*(a-b)/b

def plot_EbE_R2s():
	#set-up
	plotfontsize = 18
	cols = [0,2]
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -6.0/100., 3.5/100.
	
	#load data for R2s, different ens. avgs.
	avgdata10evs=loadtxt('10evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata100evs=loadtxt('100evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata500evs=loadtxt('500evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata1000evs=loadtxt('1000evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata10evs=loadtxt('10evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata100evs=loadtxt('100evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata500evs=loadtxt('500evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata1000evs=loadtxt('1000evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	DEAdata10evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_10evs.dat')[:,cols]
	DEAdata100evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_100evs.dat')[:,cols]
	DEAdata500evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_500evs.dat')[:,cols]
	DEAdata1000evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_1000evs.dat')[:,cols]
	
	#avgdata10evs2=loadtxt('evs_11_to_20_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	#Cavgdata10evs2=loadtxt('evs_11_to_20_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	#DEAdata10evs2=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_10evs.dat_initev_11')[:,cols]
	
	relavgdata10evs=relf(avgdata10evs[:,1],DEAdata10evs[:,1])
	relavgdata100evs=relf(avgdata100evs[:,1],DEAdata100evs[:,1])
	relavgdata500evs=relf(avgdata500evs[:,1],DEAdata500evs[:,1])
	relavgdata1000evs=relf(avgdata1000evs[:,1],DEAdata1000evs[:,1])
	relCavgdata10evs=relf(Cavgdata10evs[:,1],DEAdata10evs[:,1])
	relCavgdata100evs=relf(Cavgdata100evs[:,1],DEAdata100evs[:,1])
	relCavgdata500evs=relf(Cavgdata500evs[:,1],DEAdata500evs[:,1])
	relCavgdata1000evs=relf(Cavgdata1000evs[:,1],DEAdata1000evs[:,1])
	
	#relavgdata10evs2=relf(avgdata10evs2[:,1],DEAdata10evs2[:,1])
	#relCavgdata10evs2=relf(Cavgdata10evs2[:,1],DEAdata10evs2[:,1])
	
	#plot data
	ax.plot(avgdata10evs[:,0], relavgdata10evs, color='red', linestyle='solid', linewidth=2, label='$\overline{\\alpha}_s$, 10 events')
	ax.plot(avgdata100evs[:,0], relavgdata100evs, color='red', linestyle='--', linewidth=2, label='$\overline{\\alpha}_s$, 100 events')
	ax.plot(avgdata500evs[:,0], relavgdata500evs, color='red', linestyle='-.', linewidth=2, label='$\overline{\\alpha}_s$, 500 events')
	ax.plot(avgdata1000evs[:,0], relavgdata1000evs, color='red', linestyle=':', linewidth=2, label='$\overline{\\alpha}_s$, 1000 events')
	ax.plot(Cavgdata10evs[:,0], relCavgdata10evs, color='blue', linestyle='solid', linewidth=2, label='$\\alpha_{\langle s\\rangle}$, 10 events')
	ax.plot(Cavgdata100evs[:,0], relCavgdata100evs, color='blue', linestyle='--', linewidth=2, label='$\\alpha_{\langle s\\rangle}$, 100 events')
	ax.plot(Cavgdata500evs[:,0], relCavgdata500evs, color='blue', linestyle='-.', linewidth=2, label='$\\alpha_{\langle s\\rangle}$, 500 events')
	ax.plot(Cavgdata1000evs[:,0], relCavgdata1000evs, color='blue', linestyle=':', linewidth=2, label='$\\alpha_{\langle s\\rangle}$, 1000 events')
	#ax.plot(avgdata10evs2[:,0], relavgdata10evs2, color='green', linestyle='solid', linewidth=2, label='$\overline{R}^2_s$, 10 new events')
	#ax.plot(Cavgdata10evs2[:,0], relCavgdata10evs2, color='black', linestyle='solid', linewidth=2, label='$R^2_{\langle s\\rangle}$, 10 new events')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	#ax.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=3,ncol=2,prop={'size': plotfontsize-3})
	
	plt.savefig('rel_R2s_avgs_vars_Nev_alpha.pdf', format='pdf')
	#plt.show()
	
	#final10out = vstack((Cavgdata10evs[:,0],relCavgdata10evs)).transpose()
	#final100out = vstack((Cavgdata100evs[:,0],relCavgdata100evs)).transpose()
	#final500out = vstack((Cavgdata500evs[:,0],relCavgdata500evs)).transpose()
	#final1000out = vstack((Cavgdata1000evs[:,0],relCavgdata1000evs)).transpose()
	#outfile10 = 'rel_R2s_Cavg_10evs.dat'
	#outfile100 = 'rel_R2s_Cavg_100evs.dat'
	#outfile500 = 'rel_R2s_Cavg_500evs.dat'
	#outfile1000 = 'rel_R2s_Cavg_1000evs.dat'
	#savetxt(outfile10, final10out)
	#savetxt(outfile100, final100out)
	#savetxt(outfile500, final500out)
	#savetxt(outfile1000, final1000out)
	



def plot_EbE_R2o():
	#set-up
	plotfontsize = 18
	cols = [0,4]
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -22.5/100., 3.0/100.
	
	#load data for R2s, different ens. avgs.
	avgdata10evs=loadtxt('10evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata100evs=loadtxt('100evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata500evs=loadtxt('500evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	avgdata1000evs=loadtxt('1000evs_avgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata10evs=loadtxt('10evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata100evs=loadtxt('100evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata500evs=loadtxt('500evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	Cavgdata1000evs=loadtxt('1000evs_CavgHBTradii_cfs.dat_cfs_0')[:,cols]
	DEAdata10evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_10evs.dat')[:,cols]
	DEAdata100evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_100evs.dat')[:,cols]
	DEAdata500evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_500evs.dat')[:,cols]
	DEAdata1000evs=loadtxt('HBTradii_direct_ens_avg_ebs_0.08_cfs_0_1000evs.dat')[:,cols]
	
	relavgdata10evs=relf(avgdata10evs[:,1],DEAdata10evs[:,1])
	relavgdata100evs=relf(avgdata100evs[:,1],DEAdata100evs[:,1])
	relavgdata500evs=relf(avgdata500evs[:,1],DEAdata500evs[:,1])
	relavgdata1000evs=relf(avgdata1000evs[:,1],DEAdata1000evs[:,1])
	relCavgdata10evs=relf(Cavgdata10evs[:,1],DEAdata10evs[:,1])
	relCavgdata100evs=relf(Cavgdata100evs[:,1],DEAdata100evs[:,1])
	relCavgdata500evs=relf(Cavgdata500evs[:,1],DEAdata500evs[:,1])
	relCavgdata1000evs=relf(Cavgdata1000evs[:,1],DEAdata1000evs[:,1])
	
	#plot data
	ax.plot(avgdata10evs[:,0], relavgdata10evs, color='red', linestyle='solid', linewidth=2, label='$\overline{\\alpha}_o$, 10 events')
	ax.plot(avgdata100evs[:,0], relavgdata100evs, color='red', linestyle='--', linewidth=2, label='$\overline{\\alpha}_o$, 100 events')
	ax.plot(avgdata500evs[:,0], relavgdata500evs, color='red', linestyle='-.', linewidth=2, label='$\overline{\\alpha}_o$, 500 events')
	ax.plot(avgdata1000evs[:,0], relavgdata1000evs, color='red', linestyle=':', linewidth=2, label='$\overline{\\alpha}_o$, 1000 events')
	ax.plot(Cavgdata10evs[:,0], relCavgdata10evs, color='blue', linestyle='solid', linewidth=2, label='$\\alpha_{\langle o\\rangle}$, 10 events')
	ax.plot(Cavgdata100evs[:,0], relCavgdata100evs, color='blue', linestyle='--', linewidth=2, label='$\\alpha_{\langle o\\rangle}$, 100 events')
	ax.plot(Cavgdata500evs[:,0], relCavgdata500evs, color='blue', linestyle='-.', linewidth=2, label='$\\alpha_{\langle o\\rangle}$, 500 events')
	ax.plot(Cavgdata1000evs[:,0], relCavgdata1000evs, color='blue', linestyle=':', linewidth=2, label='$\\alpha_{\langle o\\rangle}$, 1000 events')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	#ax.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize + 5})
	#ax.set_xscale('log')
	
	ax.legend(loc=3,ncol=2,prop={'size': plotfontsize-3})
	
	plt.savefig('rel_R2o_avgs_vars_Nev_alpha.pdf', format='pdf')
	#plt.show()
	
	#final10out = vstack((Cavgdata10evs[:,0],relCavgdata10evs)).transpose()
	#final100out = vstack((Cavgdata100evs[:,0],relCavgdata100evs)).transpose()
	#final500out = vstack((Cavgdata500evs[:,0],relCavgdata500evs)).transpose()
	#final1000out = vstack((Cavgdata1000evs[:,0],relCavgdata1000evs)).transpose()
	#outfile10 = 'rel_R2o_Cavg_10evs.dat'
	#outfile100 = 'rel_R2o_Cavg_100evs.dat'
	#outfile500 = 'rel_R2o_Cavg_500evs.dat'
	#outfile1000 = 'rel_R2o_Cavg_1000evs.dat'
	#savetxt(outfile10, final10out)
	#savetxt(outfile100, final100out)
	#savetxt(outfile500, final500out)
	#savetxt(outfile1000, final1000out)




if __name__ == "__main__":
	plot_EbE_R2s()
	plot_EbE_R2o()


# End of file
