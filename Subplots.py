import numpy as np 
import matplotlib.pyplot as plt 

first_fig = plt.figure("Figure 1")

# Create 2 subplots 
# rows, cols, reference to particular subplot 
subplot1 = first_fig.add_subplot(2, 3, 1)
subplot6 = first_fig.add_subplot(2, 3, 6)

# black straight lines 
plt.plot(np.random.rand(50).cumsum(), 'k--')
plt.show()

subplot2 = first_fig.add_subplot(2, 3, 2)

# Green circles, scatter plot 
plt.plot(np.random.rand(50), 'go')
plt.show()