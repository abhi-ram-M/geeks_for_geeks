#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        res = []
        while i<n and j<m:
            if a[i]<=b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                
                i+=1
            else:
                if not res or res[-1]!= b[j]:
                    res.append(b[j])
                j += 1
        while i<n:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        while j<m:
            if not res or res[-1]!= b[j]:
                res.append(b[j])
            j += 1
        return res
            