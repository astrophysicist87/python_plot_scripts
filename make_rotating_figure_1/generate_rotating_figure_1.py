###############################################################################
# A code to generate an animation of the freeze-out hypersurface in 3D for
# different values of K_T
#####
# Author: Christopher Plumberg
#####
# Date: 01/13/2015
#####
###############################################################################
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import sys
from subprocess import call

# Set-up
eps = 0.000001

# Read in command-line arguments
localpT = float(sys.argv[1])		# Value of p_T to be used in calculations
fileToProcess = sys.argv[2]		# Full path to file to be processed
processingFolder = sys.argv[3]		# Directory to hold output files

# Load data
data = np.loadtxt(fileToProcess)

# Set-up figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plotfontsize = 18
transparency = 0.5
symbolscale = 25.0
xlower, xupper = -10.0, 10.0
ylower, yupper = -10.0, 10.0

# Process data and generate basic plot for localpT
pT = data[:,0]
tau = data[(np.where(abs(pT-localpT) <= eps))[0],1]
xT = data[(np.where(abs(pT-localpT) <= eps))[0],2]
yT = data[(np.where(abs(pT-localpT) <= eps))[0],3]
avgS = data[(np.where(abs(pT-localpT) <= eps))[0],4]
#rT = np.sqrt(xT**2 + yT**2)

# set vertical position from which to view rotating figure
vertpos=10.0

ax.scatter(xT, yT, tau, s=symbolscale*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=transparency, edgecolor='')
ax.axis([xlower, xupper, ylower, yupper])

#plt.show()
KTstring = "%0.1f" % localpT

for angle in range(0,360):
	ax.view_init(elev=vertpos, azim=angle)
	anglestring="%03d" % angle
	plt.savefig(processingFolder + '/movie_KT_' + KTstring + '_viewingangle_' + anglestring + '.png')
	print '   --> Completed angle =', angle

# Finally, convert *.png files to mp4 and zip them up
framerate = 30						# in frames/second
outputFilename = processingFolder + '/out.mp4'		# ext., '.mp4'
zipFilename = processingFolder + '/movie_KT_' + KTstring + '_files.zip'
framesFilepattern = processingFolder + '/*.png'
frameFilename = processingFolder + '/movie_KT_' + KTstring + '_viewingangle_' + '%03d.png'

convertCommandString = 'pngs2mp4 ' + str(framerate) + ' ' + frameFilename + ' ' + outputFilename
zipCommandString = 'zip -r ' + zipFilename + ' ' + framesFilepattern
cleanCommandString = 'rm ' + framesFilepattern

return_code = call(convertCommandString, shell=True)
return_code = call(zipCommandString, shell=True)
return_code = call(cleanCommandString, shell=True)

# End of file
