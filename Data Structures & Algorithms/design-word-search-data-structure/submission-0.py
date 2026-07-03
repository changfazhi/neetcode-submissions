class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None: # insert
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
        node.is_end = True
        

    def search(self, word: str) -> bool: # word may contain dots
        # this means i have to use a hashmap version
        # i need to dfs down until base case
        # my base case is that i have finally hit the full word of the search
        def dfs(i, node):
            # base case is that i hit the length of my word
            if i == len(word):
                return node.is_end
            
            # now i need to dfs down, if the ch is fucking . then i need to check all values of dict to see if it exists
            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                    
                return False
            else:
                if ch not in node.children:
                    return False
                else:
                    return dfs(i+1, node.children[ch])
            
        return dfs(0, self.root) 

        
        
