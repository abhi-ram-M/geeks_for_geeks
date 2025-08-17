class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        is_swapped = True
        for i in range(n-2,-1,-1):
            is_swapped = False
            for j in range(0,i+1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    is_swapped = True
            if not is_swapped:
                return arr
        return arr
            