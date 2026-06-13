from sympy import isprime,primerange

class prime:

    def primenum(self,a):
        return isprime(a)
    
    def primechecker(self,b):

        if isprime(b):
            print("number is prime")
        else:
            print("number is not prime")

obj1 = prime()
obj1.primechecker(7)


         

