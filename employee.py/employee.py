class employee:
    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment
    @property
    def salary_after_increment(self):
        extra = self.salary * self.increment / 100
        return self.salary + extra
    @salary_after_increment.setter
    def salary_after_increment(self,value):
        self.increment =((value - self.salary)/self.salary ) * 100

        

e =employee(4000,50)
print(e.salary_after_increment) 
print(e.increment)
print(e.salary)       