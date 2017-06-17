class Fraction:
    def __init__(self, initNum, initDenom=None):
        if initDenom != 0:
            self.num = initNum
            self.denom = initDenom
        else:
            self.num = initNum
            self.denom = 1
            print("Zero cannot be the denominator.")
            print("fraction", str(initNum)+"/0 was converted to:", str(initNum)+"/1")
    
    def __str__(self):
        if self.denom == None:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.denom)

    def getNum(self):
        return self.num
    
    def getDenom(self):
        if self.denom == None:
            return 1
        else:
            return self.denom
    
    def __add__(self, other):
        d1 = self.getDenom()
        d2 = other.getDenom()
        Newd = d1 * d2
        Newn = ((other.getDenom() * self.getNum()) + (self.getDenom() * other.getNum()))
        New = Fraction(Newn, Newd)
        good = New.Simplify()
        return good

    def Simplify(self):
        n = self.getNum()
        d = self.getDenom()
        factor = self.SharedFactor()
        if n == d:
            One = Fraction(1)
            return One
        elif (n/d)%1 == 0:
            return int(n/d) 
        elif (d/n)%1 == 0:
            good = Fraction(1, int(d/n))
            return good
        elif factor > 1:
            new = Fraction(int(n/factor), int(d/factor))
            return new
        else:
            return self

    def SharedFactor(self):
        n = self.getNum()
        d = self.getDenom()
        factor = 1
        for i in range(max(n, d), 1, -1):
            if (n%i == 0) and (d%i == 0):
                if i > factor:
                    factor = i
        return factor

    def Reciprocal(self):
        n = self.getNum()
        d = self.getDenom()
        New = Fraction(d, n)
        return New

a = Fraction(1,2)
b = Fraction(1)
c = Fraction(3,4)
d = Fraction(100, 20)
print(a + b)
print(a + c)
print(a + a)
print(c.Reciprocal())
print(d, d.Simplify(), d.Reciprocal(), (d.Reciprocal()).Simplify())
e = Fraction(8, 0)
print(e + b)