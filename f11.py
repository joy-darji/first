from sympy import primerange

class finder:

    def found(self,length,width):
        return length*width

    
for i in range(1,10):
        length = i
        width = i+10


        obj = finder()
        area = obj.found(i,i+10)
        print(area)