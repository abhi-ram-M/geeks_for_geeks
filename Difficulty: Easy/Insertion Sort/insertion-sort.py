# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        l = len(arr)
        if l>1000 or l<=1:
            return arr
        for i in range(1,l):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1] = key   
        return arr