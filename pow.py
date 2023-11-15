class PowerCalculator:
    def calculate_power(self, x, n):
       
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result

power_calculator = PowerCalculator()
result = power_calculator.calculate_power(2, 3)
print(result)  
