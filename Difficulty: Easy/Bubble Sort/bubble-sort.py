class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        i = len(arr)-1
        if i>10**3 or i<=0:
            return arr
        
        swapped = False
        while i>0:
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            i-=1
            if swapped == False:
                return arr
        return arr