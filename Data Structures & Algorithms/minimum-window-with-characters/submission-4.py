class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # so i should be expanding the window till its valid, 
        # try and be greedy and while it is valid, i should shrink it as mucn as possible
        best = float('inf')
        res = ""
        left = 0
        dic = {}
        refDic = {}
        for c in t:
            refDic[c] = refDic.get(c, 0) + 1
        
        # i need to create a helper func to check the dicts - validity check

        def sameDic(d1, d2):
            same = True
            for k,v in d1.items():
                if d2.get(k, 0) < v:
                    same = False
            return same
    
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            # while valid, shrink
            while sameDic(refDic, dic):
                # update string
                if (right - left + 1) < best:
                    best = min(best, right-left+1)
                    res = s[left:right+1]
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                
                left += 1

        
        return res