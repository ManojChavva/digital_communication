import numpy as np	
num_samples = 500
x_var = np.random.choice([-1, 1], num_samples)
n_var = np.random.normal(0, 1, num_samples)
A_db = 5
A = 10**(0.1*A_db)
y_var = A*x_var + n_var
