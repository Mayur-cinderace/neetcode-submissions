class Solution:
    def isPalindrome(self, s: str) -> bool:
        filt = ""
        for i in s:
            if i.isalnum():
                filt += i.lower()
        return filt == filt[::-1]
