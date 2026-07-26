class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = float(init)

        for _ in range(iterations):
            gradient = 2 * x
            x = x - learning_rate * gradient
        
        if iterations == 0:
            return init
            
        res = round(x, 5)
        
        return float(res)