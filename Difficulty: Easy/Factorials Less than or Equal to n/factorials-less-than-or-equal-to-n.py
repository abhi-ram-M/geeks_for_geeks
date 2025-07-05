#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        
        if n<1 or n> 10**18:
           return []
        if n == 1:
            return [1]
        fac = list()
        i = 1
        fact = 1
        while fact<=n:
            fac.append(fact)
    	    i += 1
    	    fact *= i
        return fac
    	        