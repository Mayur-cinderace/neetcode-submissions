class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dp = defaultdict(list)
        n = len(digits)
        mapping = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        if n == 0:
            return []
        dp[0] = mapping[digits[0]]

        for i in range(1, n):
            dp[i] = []
            for m in mapping[digits[i]]:
                for j in dp[i-1]: 
                    dp[i].append(j+m)
        
        return dp[n-1]