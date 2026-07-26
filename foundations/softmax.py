import numpy as np
from numpy.typing import NDArray
from math import e

class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        size = len(z)
        new_z = np.zeros(size)
        shifted_z = z - np.max(z)
        exp_z = np.exp(shifted_z)
        sum_z = np.sum(exp_z)

        new_z = exp_z/sum_z

        return np.round(new_z, 4)
        
