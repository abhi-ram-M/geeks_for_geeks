#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
	    if len(arr)<1 or len(arr)>10**6 or l<1 or l>r or r>len(arr):
	        return arr
		if l>=r :
		    return arr
		arr[l-1],arr[r-1]=arr[r-1],arr[l-1]
		return self.reverseSubArray(arr,l+1,r-1)