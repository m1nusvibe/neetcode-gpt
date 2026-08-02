import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:

        losses = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        losses_mean = np.mean(losses)

        return round(losses_mean, 4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        n = len(y_true)
        C = len(y_true[0])
        res = 0.0
        
        for i in range(n):
            for c in range(C):
                yt = y_true[i][c]
                yp = y_pred[i][c]

                res += yt * np.log(yp + 1e-7)
        
        loss = -(1/n) * res

        return round(loss, 4)
