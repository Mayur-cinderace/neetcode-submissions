class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        res[0] = 0
        if (n > 0):
            res[1] = 1
        for i in range(2, n+1):
            if i&i-1 == 0:
                res[i] = 1
                continue
            nearest = int(math.pow(2, math.floor(math.log2(i))))
            res[i] = res[nearest] + res[i-nearest]
        return res