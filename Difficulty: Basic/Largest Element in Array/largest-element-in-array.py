class Solution:
    def largest(self, arr):
        large = float('-inf')
        n = len(arr)
        if not (1 <= n<= 10**6):
            return 0
        for i in range(n):
            large = max(large,arr[i])
        return large
        
