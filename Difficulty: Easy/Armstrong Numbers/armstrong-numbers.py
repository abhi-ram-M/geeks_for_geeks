#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        if n<100 or n>1000:
            return
        sum = 0
        length = len(str(n))
        k=n

        while n>0:
            sum += (n%10)**length
            n = n//10
        if sum ==k :
            return True
        else :
            return False