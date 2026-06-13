from sympy import primerange


class prime:

    def primenum(self,length):
        pn = list(primerange(1,length))
        return pn
    
obj = prime()
finder = obj.primenum(50000)
print(finder)

