import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid()
plt.show()

# specify axis 
plt.plot(x, y)
plt.grid(axis = 'x')

plt.show()

# y axis
plt.plot(x,y)
plt.grid(axis ='y')
plt.show()

# show properties for grid 
plt.plot(x,y)
plt.grid(color = 'green',ls = '--',lw=2)
plt.show()