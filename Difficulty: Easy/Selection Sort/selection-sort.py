class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        if n<1 or n>10**3:
            return arr
        for i in range(0,n):
            min_ind = i
            for j in range(i+1,n):
                if arr[j]<arr[min_ind]:
                    min_ind = j
            arr[i],arr[min_ind]= arr[min_ind],arr[i]
        return arr