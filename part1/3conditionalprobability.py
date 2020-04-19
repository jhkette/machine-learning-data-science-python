# If I have two events that depend on each other, whats the probability that both occur

#/////Contintional probability formula ///////#

p(b|a) = p(a,b) / p(a)

# ie the probability of b given that a has occured is
# the probability of a and b both occuring divided by the probability 
# of a 


# ie Exam testing
# ie p(b|a) = 0.6 /0.8 = 0.75

# ie ^ in a test  the probability of people passing both exam a and b is 60%
# the probability of people passing just a is 80%;
# see formula above


#////// Bayes theorem /////#
p(a|b) =p(a) * p(b|a) /p(b)


# So on our example here, we're gonna come up with a drug test
# that can accurately identify users of a drug 99% of the time
# and accurately has a negative result
# for 99% of non-users.
# But, only 0.3% of the overall population
# Okay, so we have a very small probability
# of actually being a user of a drug.

# reworked formula 
#event a is the user of the drug 
#event b is tested positive for the drug
# // 0.013 is probability of testing positive if you do use + probability of testing
#  positive if you don't. ie (0.99 * 0.003 + 0.01 * 0.997)

# 0.003 * 0.99 
# /
# 0.013  

# = 22.8%

# so the odds of someone being a user given that they tested positive is 22.8%