# https://web.microsoftstream.com/video/c9883d44-2104-44a5-be96-7419e7de993b
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0,0.01)
y = 3.0* x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))
plt.plot(x,y + noise, 'r.',label='rock')
plt.plot(x,y,'b-',label="roll")

plt.title("title goes here")
plt.xlabel("along here")
plt.ylabel("yes")
plt.legend()
plt.show()
