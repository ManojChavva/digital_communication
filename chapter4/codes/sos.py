#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy
x = np.linspace(0,20,50)#points on the x axis
simlen = int(1e7) #number of samples
err = [] #declaring probability list
randvar1 = np.random.normal(0,1,simlen)
randvar2= np.random.normal (0,1,simlen)
for i in range(0,50):
	err_ind = np.nonzero((randvar1)**2+(randvar2)**2 < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
#plt.plot(x.T,err)#plotting the CDF
#plt.grid() #creating the grid
#plt.xlabel('$x$')
#plt.ylabel('$F_X(x)$')
def chi_cdf(x):
  return 1-np.exp(-(x)/2)

vec_chi=scipy.vectorize(chi_cdf)	
plt.plot(x.T, err,marker='o',label='Numerical')#plotting the CDF
plt.plot(x,vec_chi(x),label='Theory')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(['simulated' , 'Theory'])
plt.savefig('../figs/chisq_cdf.pdf')
plt.savefig('../figs/chisq_cdf.png')
plt.show()
