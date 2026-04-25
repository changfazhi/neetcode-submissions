class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            n = len(string)
            string = str(n) + "#" + string
            encoded_string += string
        return encoded_string



    def decode(self, s: str) -> List[str]:
        strs = []
        n = len(s)
        i = 0
        while i < n:
            j = s.find("#", i)
            m = int(s[i:j])
            res = s[j + 1 : j + 1 + m]
            strs.append(res)
            i = j + 1 + m
        
        return strs
