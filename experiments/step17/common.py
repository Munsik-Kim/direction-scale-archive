# Minimal public mathematical dependencies; no driver, integration or neural model.
import math
import numpy as np
P = np.array([.95, .05])
PHI0 = np.array([math.asin(.1), -.8])
def logsigmoid(x):
    return -np.logaddexp(0., -np.asarray(x))
