import numpy as np

epsilon = np.float32(1.0)
epsilon_last = epsilon

while epsilon + np.float32(1.0) > 1:
    epsilon_last = epsilon
    epsilon = epsilon/np.float32(2.0)

print("Maszynowy epsilon dla float32 to:",epsilon_last)

