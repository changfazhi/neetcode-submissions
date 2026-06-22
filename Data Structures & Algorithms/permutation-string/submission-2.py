class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for permutation, i need a dict o keep track
        # this is a fixed window sloding
        n = len(s1)
        dic = {} # this is for the window 
        left = 0
        # need to create another hash map in order to see s1
        referenceDic = {}

        def checkDic(d1, d2):
            same = True
            for k,v in d1.items():
                if k not in d2 or d1[k] != d2[k]:
                    same = False
            return same

        for c in s1:
            referenceDic[c] = referenceDic.get(c, 0) + 1
        # referenceDic now contain all char freq
        for c in s2[:n]:
            dic[c] = dic.get(c, 0) + 1
        # dic now contains char freq of the first n char
        # i should be moving the window and at each iteration compare key -> values
        # if same i can return true else i can return false
        if checkDic(referenceDic, dic):
            return True

        for right in range(n, len(s2)):
            # this will loop till the window touches the edge of s2
            # i need to check if they contain the same freq first

            dic[s2[right]] = dic.get(s2[right], 0) + 1
            dic[s2[left]] -= 1
            if dic[s2[left]] == 0:
                del dic[s2[left]]
            left += 1
            if checkDic(referenceDic, dic):
                return True

        return False
