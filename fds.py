#A
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 1]
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Graph')
plt.show()


#B
import matplotlib.pyplot as plt
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10]
c = [4, 2, 6, 8, 3]

fig, ax = plt.subplots()
ax.plot(a, label='1st Rep')
ax.plot(a, b, "or", label='2nd Rep')
ax.plot(a, list(range(0, 10, 2)), label='3rd Rep')
ax.plot(a, c, label='4th Rep')
ax.set_xlabel('Day->')
ax.set_ylabel('Temp->')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines["left"].set_bounds(-3, 40)
ax.set_xticks(list(range(-3, 10)))
ax.set_yticks(list(range(-3, 21, 3)))
ax.legend()
ax.annotate('Temperature v/s Days', xy=(1.01, -2.15))
ax.set_title('All Features Discussed')
plt.show()


#C
import matplotlib.pyplot as plt
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

fig = plt.figure(figsize=(10, 10))
sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)

sub1.plot(a, 'sb')
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

sub2.plot(b, 'or')
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')

x_for_c = list(range(0, 22, 3))
sub3.plot(x_for_c, c, 'vg')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')

sub4.plot(c, 'Dm')
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.show()


#D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('3D Surface Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()