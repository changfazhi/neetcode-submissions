class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m * n) time and O(m) space
        # double iteration
        # use freq of letters to group them

        # record the freq of each letter in a string by using a list of length 26
        # append all the freq of each string to a bigger table
        # use the table to compare, those same append to res

        res = []
        hashTable = {}
        
        for string in strs:
            alphalist = [0] * 26
            for char in string:
                idx = ord(char) - ord('a')
                alphalist[idx] += 1
            if tuple(alphalist) not in hashTable:
                hashTable[tuple(alphalist)] = []
            hashTable[tuple(alphalist)].append(string)
        
        for value in hashTable.values():
            res.append(value)
        
        return res
        

        

        

        



        