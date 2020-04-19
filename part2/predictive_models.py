#linear regression
# uses least squares - minimises squared error
# between each point and the line

# A GOOD GUIDE TO FORMULA
# https://www.dummies.com/education/math/statistics/how-to-calculate-a-regression-line/


# line is a slope value and a y intercept

#slope intercept equation of a line y=mx+b
#(ie in example - see predict function - slope * pagespeed + intercept)

# slope is correlation between two variable times the standard deviation
# in Y divided by standard deviation in X. 

# the intercept is the mean of y mius the slope times mean of x


# measuring error with r2

#the fraction of the total variation in Y that is captured by your model

# sum of squared errors/ sum of squared variation from mean


import matplotlib.pyplot as plt
# don't need to do this can use polyfit
def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='g')
plt.show()


# polynomial regression

%matplotlib inline
from pylab import *
import numpy as np

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 1))
