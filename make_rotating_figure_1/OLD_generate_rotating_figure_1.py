###############################################################################
# A test code to generate an animation of a simple figure in 3D rotating
# Author: Christopher Plumberg
# Date: 01/04/2015
###############################################################################
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#import pylab as pl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import *
from scipy import interpolate
from subprocess import call


# Just generate figure first...
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plotfontsize = 18
xlower, xupper = -10.0, 10.0
ylower, yupper = -10.0, 10.0
event = 759
localpT = 0.0
eps = 0.000001

direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V1/NEW_TDEP_V1_results-%(event)d' % {"event": event}
fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
data = np.loadtxt(fileToProcess)

pT = data[:,0]
tau = data[(np.where(abs(pT-localpT) <= eps))[0],1]
xT = data[(np.where(abs(pT-localpT) <= eps))[0],2]
yT = data[(np.where(abs(pT-localpT) <= eps))[0],3]
avgS = data[(np.where(abs(pT-localpT) <= eps))[0],4]
#rT = np.sqrt(xT**2 + yT**2)

#X, Y, Z = axes3d.get_test_data(0.05)
#ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3)

# set vertical position from which to view rotating figure
vertpos=10.0

ax.scatter(xT, yT, tau, s=25.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
ax.axis([xlower, xupper, ylower, yupper])

def init():
    ax.view_init(elev=vertpos, azim=0)
    return ax,

def animate(i):
    ax.view_init(elev=vertpos, azim=i)
    return ax,

#anim = animation.FuncAnimation(fig, animate, np.arange(0,360,10), init_func=init, interval=25, blit=True)

#plt.show()

#anim.save('~/rotating_3d_animation.mp4', fps=30)

for angle in range(0,360):
	ax.view_init(elev=vertpos, azim=angle)
	anglestring="%03d" % angle
	plt.savefig('movie' + anglestring + '.png')
	print 'Completed angle =', angle

#ax.scatter(xT, yT, tau, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
#ax.axis([xlower, xupper, ylower, yupper])
#KTstring = "%0.1f" % localpT
#outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_0.20.pdf'
#plt.savefig(outfile, format='pdf')
#print 'Generated and saved', outfile




# End of file
