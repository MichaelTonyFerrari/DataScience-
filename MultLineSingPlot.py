import numpy as np
import matplotlib.pyplot as plt 

data_size = 15
# mean, standard divation 
low_mu, low_sigma = 50, 4.3
low_data_size = low_mu + low_sigma * np.random.randn(data_size)

high_mu, high_sigma = 57, 5.2 
high_data_size = high_mu + high_sigma * np.random.rand(data_size)

# horzonital 
days = list(range(1, data_size + 1))

plt.plot(days, low_data_size, days, high_data_size)
plt.show()

plt.plot(days, low_data_size,
		days, low_data_size, "vm",
		days, high_data_size,
		days, high_data_size, "^k"
	)
plt.show()

plt.plot(days, low_data_size,
		days, high_data_size
		)
plt.xlabel("Day")
plt.ylabel("Temperature: Farenheit")
plt.title("Random temp data")
plt.show()

plt.plot(
		days, high_data_size, "^k"
		)
plt.xlabel("Day")
plt.ylabel("Temperature: Farenheit")
plt.title("Random temp data")
plt.show()

t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

l1 = plt.plot(t2, np.exp(-t2))
l2, l3 = plt.plot(t2, np.sin(2*np.pi*t2), '--go', t1, np.log(1+t1), '.')
l4 = plt.plot(t2, np.exp(-t2) * np.sin(2*np.pi*t2), 'rs--')

