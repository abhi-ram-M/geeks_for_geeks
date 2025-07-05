#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		l = 0
		r= len(s)-1
		if r>10**6:
		    return False
		while l<r:
		    if s[l]!=s[r]:
		        return False
		    l+=1
		    r-=1
		return True
		
		