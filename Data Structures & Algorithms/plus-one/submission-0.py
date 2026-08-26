class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        if digits[-1] != 9:
            res.extend(digits[:-1])
            res.append(digits[-1]+1) 
        else:
            i = n-1
            while i >= 0 and digits[i] == 9:
                res.insert(0, 0)
                i -= 1
            if (i == -1):
                res.insert(0, 1)
            else:
                res.insert(0, digits[i]+1)
                res = digits[:i] + res
                # res.reverse()
        return res