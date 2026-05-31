class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(el):

            l, r = 0, len(el) - 1
            while l <= r:
                if el[l] == el[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        def backtrack(idx, path):
            # base case is each element in the path is a palindrome... tuff
            if idx == len(s):
                res.append(path[:])
                return
            # iterate the choices
            for i in range(idx, len(s)): # i represent the last pos of the substring
                # pick a choice
                substring = s[idx: i+1]
                # pruning is to guard boundaries
                if not is_palindrome(substring):
                    continue
                # choose a choice
                path.append(substring)
                # explore
                backtrack(i+1, path)
                # undo
                path.pop()

        backtrack(0, [])
        return res