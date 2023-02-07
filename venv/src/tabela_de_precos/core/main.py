
# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
 
 
fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
 
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
line, = ax1.plot(t, s, color='green', lw=2)
 
np.random.seed(19680801)
 
ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50,
                            facecolor='yellow',
                            edgecolor='yellow')
 
fig.suptitle('matplotlib.figure.Figure.add_axes() \
function Example\n\n', fontweight=& quot
             bold & quot
             )
 
plt.show()