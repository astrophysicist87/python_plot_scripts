#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.font_manager import FontProperties

def relf(a,b):			# returns the percent difference between vectors a and b, element-wise
	#return 200.*(a-b)/(a+b)
	return 100.*(a-b)/b


def generate_R2s_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
	ax2 = fig.add_axes([0.5, 0.5, 0.375, 0.375])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 3.0, 13.5
	pclower, pcupper = -10.5, 10.5
	
	#load data
	SSH000=loadtxt('HBTradii_cfs_ev1.dat_cfs_0')
	Cbar000=loadtxt('avgHBTradii_cfs.dat_cfs_0')
	Cavg000=loadtxt('CavgHBTradii_cfs.dat_cfs_0')
	DEA000=loadtxt('HBTradii_direct_ens_avg_ebs_0.00_cfs_0_1000evs.dat')
	DV000=loadtxt('HBTradii_direct_variance_ebs_0.00_cfs_0_1000evs.dat')
	#REL000=loadtxt('ENSavgs_rel_to_DEA_1000evs.dat')
	
	#plot data
	#R2s
	ax1.plot(SSH000[:,0],SSH000[:,2], color='red', linestyle='solid', linewidth=2, label='$R^2_{\overline{s}}$')
	ax1.plot(Cbar000[:,0],Cbar000[:,2], color='blue', linestyle='solid', linewidth=2, label='$\overline{R}^2_s$')
	ax1.plot(Cavg000[:,0],Cavg000[:,2], color='green', linestyle='solid', linewidth=2, label='$R^2_{\langle s\\rangle}$')
	ax1.plot(DEA000[:,0],DEA000[:,2], color='black', linestyle='solid', linewidth=2, label='$\langle R^2_s\\rangle$')
	ax1.plot(DEA000[:,0],DEA000[:,2]+sqrt(DV000[:,2]), color='black', linestyle='--', linewidth=2)
	ax1.plot(DEA000[:,0],DEA000[:,2]-sqrt(DV000[:,2]), color='black', linestyle='--', linewidth=2)
	ax1.fill_between(DEA000[:,0], DEA000[:,2]-sqrt(DV000[:,2]), DEA000[:,2]+sqrt(DV000[:,2]), color='grey', alpha='0.25')
	#ax2.plot(REL000[:,0],100.*REL000[:,1], color='red', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,2], color='blue', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,3], color='green', linewidth=2)
	ax2.axhline(0.0, color='black', linewidth=2)
	ax2.plot(DEA000[:,0],relf(SSH000[:,2],DEA000[:,2]), color='red', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cbar000[:,2],DEA000[:,2]), color='blue', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cavg000[:,2],DEA000[:,2]), color='green', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,2]-sqrt(DV000[:,2]),DEA000[:,2]), color='black', linestyle='--', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,2]+sqrt(DV000[:,2]),DEA000[:,2]), color='black', linestyle='--', linewidth=2)
	ax2.fill_between(DEA000[:,0], relf(DEA000[:,2]-sqrt(DV000[:,2]),DEA000[:,2]), relf(DEA000[:,2]+sqrt(DV000[:,2]),DEA000[:,2]), color='grey', alpha='0.25')
	
	#update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax2.axis([xlower, xupper, pclower, pcupper])
	ax1.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax1.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax2.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	ax2.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize - 7})
	
	fontP = FontProperties()
	fontP.set_size(plotfontsize)
	ax1.legend(loc=3, prop=fontP)
	
	plt.savefig('R2s_ens_avg_comps_w_inset.pdf', format='pdf')
	#plt.show()


def generate_R2o_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
	ax2 = fig.add_axes([0.5, 0.5, 0.375, 0.375])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 5.0, 34.0
	pclower, pcupper = -17.5, 17.5
	
	#load data
	SSH000=loadtxt('HBTradii_cfs_ev1.dat_cfs_0')
	Cbar000=loadtxt('avgHBTradii_cfs.dat_cfs_0')
	Cavg000=loadtxt('CavgHBTradii_cfs.dat_cfs_0')
	DEA000=loadtxt('HBTradii_direct_ens_avg_ebs_0.00_cfs_0_1000evs.dat')
	DV000=loadtxt('HBTradii_direct_variance_ebs_0.00_cfs_0_1000evs.dat')
	#REL000=loadtxt('ENSavgs_rel_to_DEA_1000evs.dat')
	
	#plot data
	#R2o
	ax1.plot(SSH000[:,0],SSH000[:,4], color='red', linestyle='solid', linewidth=2, label='$R^2_{\overline{o}}$')
	ax1.plot(Cbar000[:,0],Cbar000[:,4], color='blue', linestyle='solid', linewidth=2, label='$\overline{R}^2_o$')
	ax1.plot(Cavg000[:,0],Cavg000[:,4], color='green', linestyle='solid', linewidth=2, label='$R^2_{\langle o\\rangle}$')
	ax1.plot(DEA000[:,0],DEA000[:,4], color='black', linestyle='solid', linewidth=2, label='$\langle R^2_o\\rangle$')
	ax1.plot(DEA000[:,0],DEA000[:,4]+sqrt(DV000[:,4]), color='black', linestyle='--', linewidth=2)
	ax1.plot(DEA000[:,0],DEA000[:,4]-sqrt(DV000[:,4]), color='black', linestyle='--', linewidth=2)
	ax1.fill_between(DEA000[:,0], DEA000[:,4]-sqrt(DV000[:,4]), DEA000[:,4]+sqrt(DV000[:,4]), color='grey', alpha='0.25')
	#ax2.plot(REL000[:,0],100.*REL000[:,4], color='red', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,5], color='blue', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,6], color='green', linewidth=2)
	ax2.axhline(0.0, color='black', linewidth=2)
	ax2.plot(DEA000[:,0],relf(SSH000[:,4],DEA000[:,4]), color='red', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cbar000[:,4],DEA000[:,4]), color='blue', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cavg000[:,4],DEA000[:,4]), color='green', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,4]-sqrt(DV000[:,4]),DEA000[:,4]), color='black', linestyle='--', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,4]+sqrt(DV000[:,4]),DEA000[:,4]), color='black', linestyle='--', linewidth=2)
	ax2.fill_between(DEA000[:,0], relf(DEA000[:,4]-sqrt(DV000[:,4]),DEA000[:,4]), relf(DEA000[:,4]+sqrt(DV000[:,4]),DEA000[:,4]), color='grey', alpha='0.25')
	
	#update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax2.axis([xlower, xupper, pclower, pcupper])
	ax1.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax1.set_ylabel(r'$R^2_o$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax2.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	ax2.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize - 7})
	
	fontP = FontProperties()
	fontP.set_size(plotfontsize)
	ax1.legend(loc=3, prop=fontP)
	
	plt.savefig('R2o_ens_avg_comps_w_inset.pdf', format='pdf')
	#plt.show()



def generate_R2l_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
	ax2 = fig.add_axes([0.275, 0.5, 0.375, 0.375])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 75.0
	pclower, pcupper = -12.5, 12.5
	
	#load data
	SSH000=loadtxt('HBTradii_cfs_ev1.dat_cfs_0')
	Cbar000=loadtxt('avgHBTradii_cfs.dat_cfs_0')
	Cavg000=loadtxt('CavgHBTradii_cfs.dat_cfs_0')
	DEA000=loadtxt('HBTradii_direct_ens_avg_ebs_0.00_cfs_0_1000evs.dat')
	DV000=loadtxt('HBTradii_direct_variance_ebs_0.00_cfs_0_1000evs.dat')
	#REL000=loadtxt('ENSavgs_rel_to_DEA_1000evs.dat')
	
	#plot data
	#R2l
	ax1.plot(SSH000[:,0],SSH000[:,8], color='red', linestyle='solid', linewidth=2, label='$R^2_{\overline{l}}$')
	ax1.plot(Cbar000[:,0],Cbar000[:,8], color='blue', linestyle='solid', linewidth=2, label='$\overline{R}^2_l$')
	ax1.plot(Cavg000[:,0],Cavg000[:,8], color='green', linestyle='solid', linewidth=2, label='$R^2_{\langle l\\rangle}$')
	ax1.plot(DEA000[:,0],DEA000[:,8], color='black', linestyle='solid', linewidth=2, label='$\langle R^2_l\\rangle$')
	ax1.plot(DEA000[:,0],DEA000[:,8]+sqrt(DV000[:,8]), color='black', linestyle='--', linewidth=2)
	ax1.plot(DEA000[:,0],DEA000[:,8]-sqrt(DV000[:,8]), color='black', linestyle='--', linewidth=2)
	ax1.fill_between(DEA000[:,0], DEA000[:,8]-sqrt(DV000[:,8]), DEA000[:,8]+sqrt(DV000[:,8]), color='grey', alpha='0.25')
	#ax2.plot(REL000[:,0],100.*REL000[:,7], color='red', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,8], color='blue', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,9], color='green', linewidth=2)
	ax2.axhline(0.0, color='black', linewidth=2)
	ax2.plot(DEA000[:,0],relf(SSH000[:,8],DEA000[:,8]), color='red', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cbar000[:,8],DEA000[:,8]), color='blue', linewidth=2)
	ax2.plot(DEA000[:,0],relf(Cavg000[:,8],DEA000[:,8]), color='green', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,8]-sqrt(DV000[:,8]),DEA000[:,8]), color='black', linestyle='--', linewidth=2)
	ax2.plot(DEA000[:,0],relf(DEA000[:,8]+sqrt(DV000[:,8]),DEA000[:,8]), color='black', linestyle='--', linewidth=2)
	ax2.fill_between(DEA000[:,0], relf(DEA000[:,8]-sqrt(DV000[:,8]),DEA000[:,8]), relf(DEA000[:,8]+sqrt(DV000[:,8]),DEA000[:,8]), color='grey', alpha='0.25')
	
	#update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax2.axis([xlower, xupper, pclower, pcupper])
	ax1.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax1.set_ylabel(r'$R^2_l$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax2.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	ax2.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize - 7})
	
	fontP = FontProperties()
	fontP.set_size(plotfontsize)
	ax1.legend(loc=1, prop=fontP)
	
	plt.savefig('R2l_ens_avg_comps_w_inset.pdf', format='pdf')
	#plt.show()



def generate_R2ol_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax1 = fig.add_axes([0.125,0.125,0.825,0.825])
	ax2 = fig.add_axes([0.375, 0.225, 0.35, 0.35])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -30.0, 0.0
	pclower, pcupper = -13.0, 12.0
	
	#load data
	SSH000=loadtxt('HBTradii_cfs_ev1.dat_cfs_0')
	Cbar000=loadtxt('avgHBTradii_cfs.dat_cfs_0')
	Cavg000=loadtxt('CavgHBTradii_cfs.dat_cfs_0')
	DEA000=loadtxt('HBTradii_direct_ens_avg_ebs_0.00_cfs_0_1000evs.dat')
	DV000=loadtxt('HBTradii_direct_variance_ebs_0.00_cfs_0_1000evs.dat')
	#REL000=loadtxt('ENSavgs_rel_to_DEA_1000evs.dat')

	onezero=zeros(len(DEA000[:,0]))+1
	onezero[0]=0.
	
	#plot data
	#R2ol
	ax1.plot(SSH000[:,0],SSH000[:,12], color='red', linestyle='solid', linewidth=2, label='$R^2_{\overline{ol}}$')
	ax1.plot(Cbar000[:,0],Cbar000[:,12], color='blue', linestyle='solid', linewidth=2, label='$\overline{R}^2_{ol}$')
	ax1.plot(Cavg000[:,0],Cavg000[:,12], color='green', linestyle='solid', linewidth=2, label='$R^2_{\langle ol\\rangle}$')
	ax1.plot(DEA000[:,0],DEA000[:,12], color='black', linestyle='solid', linewidth=2, label='$\langle R^2_{ol}\\rangle$')
	ax1.plot(DEA000[:,0],DEA000[:,12]+sqrt(DV000[:,12]), color='black', linestyle='--', linewidth=2)
	ax1.plot(DEA000[:,0],DEA000[:,12]-sqrt(DV000[:,12]), color='black', linestyle='--', linewidth=2)
	ax1.fill_between(DEA000[:,0], DEA000[:,12]-sqrt(DV000[:,12]), DEA000[:,12]+sqrt(DV000[:,12]), color='grey', alpha='0.25')
	#ax2.plot(REL000[:,0],100.*REL000[:,10], color='red', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,11], color='blue', linewidth=2)
	#ax2.plot(REL000[:,0],100.*REL000[:,12], color='green', linewidth=2)
	ax2.axhline(0.0, color='black', linewidth=2)
	ax2.plot(DEA000[:,0],onezero*relf(SSH000[:,12],DEA000[:,12]), color='red', linewidth=2)
	ax2.plot(DEA000[:,0],onezero*relf(Cbar000[:,12],DEA000[:,12]), color='blue', linewidth=2)
	ax2.plot(DEA000[:,0],onezero*relf(Cavg000[:,12],DEA000[:,12]), color='green', linewidth=2)
	ax2.plot(DEA000[:,0],onezero*relf(DEA000[:,12]-sqrt(DV000[:,12]),DEA000[:,12]), color='black', linestyle='--', linewidth=2)
	ax2.plot(DEA000[:,0],onezero*relf(DEA000[:,12]+sqrt(DV000[:,12]),DEA000[:,12]), color='black', linestyle='--', linewidth=2)
	ax2.fill_between(DEA000[:,0], onezero*relf(DEA000[:,12]+sqrt(DV000[:,12]),DEA000[:,12]), onezero*relf(DEA000[:,12]-sqrt(DV000[:,12]),DEA000[:,12]), color='grey', alpha='0.25')
	
	#print onezero*relf(DEA000[:,12]+sqrt(DV000[:,12]),DEA000[:,12]), onezero*relf(DEA000[:,12]-sqrt(DV000[:,12]),DEA000[:,12])
	
	#update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax2.axis([xlower, xupper, pclower, pcupper])
	ax1.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax1.set_ylabel(r'$R^2_{ol}$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	ax2.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	ax2.set_ylabel(r'p.c. deviation from d.e.a.', {'fontsize': plotfontsize - 7})
	
	fontP = FontProperties()
	fontP.set_size(plotfontsize)
	ax1.legend(loc=4, prop=fontP)
	
	plt.savefig('R2ol_ens_avg_comps_w_inset.pdf', format='pdf')
	#plt.show()



if __name__ == "__main__":
	generate_R2s_plots()
	generate_R2o_plots()
	generate_R2l_plots()
	generate_R2ol_plots()
