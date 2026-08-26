class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s+'~'
        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        lst = []
        new = ""
        for c in s:
            if c!='~':
                new += c
            else:
                lst.append(new)
                new =""
        return lst
