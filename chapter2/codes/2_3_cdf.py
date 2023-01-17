import numpy as np
import matplotlib.pyplot as plt
#limits
maxlim = 30
maxpts = 50
x = np.linspace(-5, maxlim, maxpts) #points on x-axis
simlen = int(1e6) #number of samples
cdf = [] #declaring probability list

# -2ln(1-U)
datfile = np.loadtxt('uni.dat',dtype='double')
frv = -2*np.log(1-datfile)

for i in range(0,maxpts):
	cdf_ind = np.nonzero(frv < x[i]) #checking probability condition
	cdf_n = np.size(cdf_ind) #computing the probability
	cdf.append(cdf_n/simlen) #storing the probability values in a list

def exp_cdf(x):
	return np.piecewise(x, [x<0, x>=0], [0, lambda x: 1-np.exp(-x/2)])

plt.plot(x, cdf, 'o') #plotting CDF numerical
plt.plot(x, exp_cdf(x)) #plottong CDF theory
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../figs/log.pdf')
plt.show() #opening the plot window
