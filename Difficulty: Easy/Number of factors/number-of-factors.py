class Solution:
    def countFactors (self, n):
        from math import sqrt
        if n<1 or n>10**5:
            return
        fac = 0
        for i in range(1,int(sqrt(n))+1):
            if n%i == 0:
                if n//i == i:
                    fac += 1
                else :
                    fac += 2
        return fac