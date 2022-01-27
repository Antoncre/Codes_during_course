class Salary:
    # define Salary class and associated methods here
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, d):
        return d * self.rate


class Promotable:
    # define Promotable class and associated methods here
    def __init__(self, rate):
        self.rate = rate

    def promote(self, promotion):
        self.rate = self.rate + promotion


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


anton = Employee(15.0)
print(anton.weekly_salary())
anton.promote(5)
print(anton.weekly_salary())
