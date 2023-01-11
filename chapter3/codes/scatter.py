import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if
A = 5
A1=10**(0.1*A);
simlen = int(100)
n= np.random.normal(0, 1, simlen)
values = [-1, 1]
probabilities = [0.5, 0.5]
X=np.random.choice(values, simlen, p=probabilities)
y_var = A1*X + n

x0 = np.extract(X==1, X)
x1 = np.extract(X==-1, X)
n0 = np.extract(X==1, n)
n1 = np.extract	(X==-1, n)
y0 = A1*x0 + n0
y1 = A1*x1 + n1

plt.scatter(np.arange(y0.shape[0]),y0)
plt.scatter(np.arange(y1.shape[0]),y1)
#plt.plot(np.zeros(y0.shape[0]),y0, 'o', mfc='none')
#plt.plot(np.zeros(y1.shape[0]),y1, 'o', mfc='none')
plt.plot(np.linspace(-10, 60, 10),np.zeros(10), color='black')
plt.grid()
plt.legend(["$y|0$","$y|1$"])
plt.savefig('../figs/bpsk_scatter.pdf')
plt.savefig('../figs/bpsk_scatter.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/ch3/bpsk_scatter.pdf"))
#else
plt.show() #opening the plot window
