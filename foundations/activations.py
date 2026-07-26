import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        new_z = np.zeros(len(z))

        new_z = 1/(1+math.e**(-z))
        
        return np.round(new_z, 5)


    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        new_z = np.zeros(len(z))

        for i in range(len(z)):
            new_z[i] = max(0, z[i])
        
        return new_z
