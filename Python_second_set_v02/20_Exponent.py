


class PowerOfTwo:
    def __init__(self,num):
        self.n = num
    
    def power_calc(self):
        for i in range(0, self.n+1):
            res = 2**i
            print(f"2 ^ {i} = {res}")

P = PowerOfTwo(3)
P.power_calc()