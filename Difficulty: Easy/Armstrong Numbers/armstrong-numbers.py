#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        original = n
        power = len(str(n))
        result = 0
        while n>0:
            result = result + (n % 10)**power
            n = n//10
        return result == original
        