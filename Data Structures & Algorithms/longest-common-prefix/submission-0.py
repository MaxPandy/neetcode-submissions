class TrieNode():
    def __init__(self):
        self.children=[None]*26
        self.EndOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.EndOfWord=True

    def check(self,word: str) -> int:
        curr=self.root
        length=0
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                return length
            curr=curr.children[index]
            length+=1
        return length
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return 0

        tree=Trie()
        tree.insert(strs[0])
        minimum=len(strs[0])
        for i in range (1,len(strs)):
            minimum=min(minimum,tree.check(strs[i]))
        
        return strs[0][:minimum]