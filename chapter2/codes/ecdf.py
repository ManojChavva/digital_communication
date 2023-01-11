
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss



x = np.linspace(-4,4,100)   #points on the x axis
print(x)

simlen = int(1e6)    #number of samples
print(simlen)

err = [] #declaring probability list


randvar = np.loadtxt('gau.dat',dtype='double')
print(randvar)

y = ss.norm.cdf(x)
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
print(err_ind)
print(err_n)
print(err)	
plt.scatter(x.T,err)#plotting the CDF
plt.plot(x,y,color='r')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Theory","practicl"])
plt.savefig('../figs/gauss_cdf.pdf')
plt.savefig('../figs/gauss_cdf.png')
plt.show() #opening the plot window
