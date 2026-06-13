class squcube:
    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2

    def square(self):
        squarefinder = self.num1*self.num1
        return(squarefinder)

    def cube(self):
        cubefinder = self.num2*self.num2
        return(cubefinder)

finder = squcube(23,24)
print(finder.square())
print(finder.cube())



