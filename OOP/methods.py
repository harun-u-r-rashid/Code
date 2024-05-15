
class pythonClass:

        def __init__(self, value):
                self.value = value


        def pythonMethod(self):
                print("This is the method")
                print("Value is : ", self.value)


pythonObject = pythonClass(10) #Here set the value is 10
pythonObject.pythonMethod() #Here, I just called the python method
