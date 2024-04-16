import numpy as np

X = [95,85,98]
y = [100,90,78]

print(np.cov(y,X,ddof=1))