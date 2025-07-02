#User function Template for python3

class Solution:
    def printGfg(self, n):
        if n<1 or n>1000 :
            return
        print('GFG',end=' ')
        self.printGfg(n-1)