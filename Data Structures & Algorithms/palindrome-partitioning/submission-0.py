class Solution:
    def backtrack(self, start, n, s, curr, answer):
        if start == n:
            answer.append(curr[:])
            return
        for end in range(start, n):
            if s[start:end+1] == s[start:end+1][::-1]:
                # print(s[start:end], s[start:end][::-1])
                curr.append(s[start:end+1])
                # print(curr)
                self.backtrack(end+1, n, s, curr, answer)
                curr.pop()

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        answer = []
        self.backtrack(0, n, s, [], answer)
        return answer