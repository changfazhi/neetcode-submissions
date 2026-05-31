class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def backtrack(idx, path):
            # base case is when my path is the same length as the digts
            if len(path) == len(digits):
                res.append(path)
                return
            
            digit = digits[idx]
            letters = mapping[digit]

            for letter in letters:
                # make a choice
                path += letter
                # explore 
                backtrack(idx+1, path)
                # undo
                path = path[:-1]
            
        backtrack(0, "")
        if res == [""]:
            return []
        else:
            return res



        