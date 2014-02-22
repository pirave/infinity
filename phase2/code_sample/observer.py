
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.subplots_adjust(bottom=0.2)

x = np.linspace(-10, 10, 200)
line, = plt.plot(x, x, "c")

plt.xlabel(r"$x$", fontsize = 15)
plt.ylabel(r"$x$", fontsize = 15)
plt.grid(True)

class Power:
    power = 1
    def incr(self, event):
        self.power += 1
        line.set_ydata(x**self.power)
        plt.draw()

    def decr(self, event):
        self.power -= 1
        line.set_ydata(x**self.power)
        plt.draw()

    def updateLabel(self, event):
        ax.set_ylabel(r"$x^{" + str(self.power) + r"}$", fontsize=15)
        plt.draw()


callback = Power()
axUp = plt.axes([0.7, 0.05, 0.1, 0.075])
axDown = plt.axes([0.81, 0.05, 0.1, 0.075])

bUp = Button(axDown, 'Up')
bUp.on_clicked(callback.incr)
bUp.on_clicked(callback.updateLabel)

bDown = Button(axUp, 'Down')
bDown.on_clicked(callback.decr)
bDown.on_clicked(callback.updateLabel)

plt.show()

