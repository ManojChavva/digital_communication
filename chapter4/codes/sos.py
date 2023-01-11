#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

maxrange=50
maxlim=300.0
x = np.linspace(0,maxlim,maxrange)    #points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
x1_var = np.random.normal(0, 1, simlen)
x2_var = np.random.normal(0, 1, simlen)
v_var = x1_var**2 + x2_var**2

for i in range(0,maxrange):
	err_ind = np.nonzero(v_var < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
pdf = np.gradient(err, x, edge_order=2)
a=(1/2)*np.exp(-x/2)
b=1-np.exp(-x/2)
plt.plot(x.T,err,'orange')   #plotting the CDF
y=np.piecewise(x,[x<0,x>=0],[0,lambda a:a])
plt.scatter(y,err)
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../figs/chisq_cdf.pdf')
plt.savefig('../figs/chisq_cdf.png')

plt.show()
plt.close()
z=np.piecewise(x,[x<0,x>=0],[0,lambda b:b])
plt.scatter(z,pdf)
plt.plot(x,pdf,'orange')             # plotting estimated PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.savefig('../figs/chisq_pdf.pdf')
plt.savefig('../figs/chisq_pdf.png')

plt.show()

