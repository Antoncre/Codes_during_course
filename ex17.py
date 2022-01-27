from addition import Addition
class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)
    @classmethod
    def subtract(cls, num1, num2):
        num2 = -num2
        return Addition.add(num1, num2)
    @classmethod
    def multiply(cls, num1, num2):
        tm = []
        for m in range(num2):
            tm.append(Addition.add(num1, 0))
        return sum(tm)
    @classmethod
    def divide(cls, num1, num2):
        if num1 == num2:
            return 1
        elif num1 < num2:
            return 0
        else:
            to_d = []
            for s in range(Calculator.subtract(num2, 1), Addition.add(num1, 0), num2):
                to_d.append(s)
            return len(to_d)



nita = Calculator.add(2, 2)
print(nita)

nits = Calculator.subtract(2, 2)
print(nits)
nitm = Calculator.multiply(2, 2)
print(nitm)
nitd = Calculator.divide(2, 2)
print(nitd)

