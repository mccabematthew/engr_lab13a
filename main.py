import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# figure for t axis to enhance graph readability
fig = plt.figure()
ax = fig.add_subplot()

# getting user coef. for poly. and mapping to array, then solving poly and getting derivs
coefficients = list(map(int, input('Enter all coefficients with a space inbetween (accept for at end): ').split(' ')))
c = np.array(coefficients)
poly = np.poly1d(c)
deriv1 = poly.deriv()
deriv2 = deriv1.deriv()

# functions for identifying local min and max
# for loop for iterating through points on plot
# run min and max funcs through for loop




# evaluating poly and derivs, and plotting functions with limits
x = np.linspace(-5, 5)
y1 = np.polyval(poly, x)
y2 = np.polyval(deriv1, x)
y3 = np.polyval(deriv2, x)
plt.plot(x, y1, label='f(x)')
plt.plot(x, y2, '--', label="f'(x)")
plt.plot(x, y3, ':', label="f''(x)")

# formatting the plot and elements within
plt.title("Plots of f(x), f'(x), f''(x) with local max and min")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(shadow='True', loc='upper left')
plt.axhline()
plt.axvline()
plt.axis()
plt.grid()

plt.show()
