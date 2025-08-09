#self keyword is mandatory for calling variable into method
#instance and class variables have whole different purpose
#constructor name should start __init
#new keyword is not required when you create obj


class Calculator:
    num = 100 #class veriables

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

        print("I am called automatically when object created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num #or self.num

obj = Calculator(2,3) #syntax to create obj in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create obj in python
obj1.getData()
print(obj1.Summation())




