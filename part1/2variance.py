#variance is the average of the squared difference from the mean.
# so..
# find mean

# find difference from mean

# then SQUARE them - this stops ngative numbers cancelled out positive ones - also gives wieght to outliers

# find the average of the squared differences. 

# standard deviation is SQUARE root of variance


# Variance pop vs sample variance

# sample variance is different because you divide by sample -1

# probability distribution function = probability of data falling within a given value
#pribabilty desnity function for discrete data

# pdf can be normal, uniform (ie uniform even chance) of exponential

#percentiles divide data according to % at what is x% of the values are less than that value. ie income 
# distribution the 99%


import numpy as np
vals = np.random.normal(0, 0.5, 10000)
np.percentiles(vals, 50)


# Covariance

# see https://www.youtube.com/watch?v=0nZT9fqr2MU
# see https://www.youtube.com/watch?v=9Y0Alg8huJk - this is the best video

# covariance = sum ((x -mean) * (y - mean)) /n -1 

# correlation is dividing the covariance by the standard deviation of both variables - should
# be range -1 (negative correlation) 0 (no correlation) and 1 positive correlation

# a simpler equation uses dot product

def de_mean(x): #work out deviation from mean
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x) # length ie number of data
    return dot(de_mean(x), de_mean(y)) / (n-1)   #dot product of deviation from mean for a set of data points 
    # by another set of 