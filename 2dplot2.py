# https://web.microsoftstream.com/video/7a57ee2c-df42-48d3-882b-cdcabe97c39b
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0,0.01)
y = 3.0* x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))
plt.plot(x,y + noise, 'r.')
#allows a second plot to be made on the same plot
plt.plot(x,y,'b-')
plt.show()
#clears plot
plt.plot(x,y + noise, 'g.')
plt.plot(x,y,'c-')
plt.show()