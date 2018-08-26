import math
import random

def in_circle(x, y, rad):
    if x**2 + y**2 < rad**2:
        return True
    else:
        return False


def monte_carlo_integration(sample, rad):
    count = 0
    for i in range(sample):
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        if in_circle(x, y, rad):
            count += 1
    ratio = count/sample
    estimate = (4*count)/(sample*rad*rad)
    percent_error = ((math.pi - estimate)/math.pi)*100
    print("The Estimate of Pi is: %s" % estimate)
    print("Ratio: %s" % ratio)
    print("The error is: %s" % abs((math.pi - estimate)))
    print("Percent error is: %s" % abs(percent_error))

monte_carlo_integration(1945830, 1)
