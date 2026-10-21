class Solution:
    # O(m) time for encode and decode
    # O(m+n) space for encode and decode

    def encode(self, strs: List[str]) -> str:
        # the output for this should look like 5Hello5World
        res = ""
        # base case
        
        for string in strs:
            n = len(string)
            res += f"{n}#"
            for char in string:
                res += char
        
        return res

        
    def decode(self, s: str) -> List[str]:
        # base case


        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            word = s[start: start + length]
            res.append(word)
            i = start + length

        return res

