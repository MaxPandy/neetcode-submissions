class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.IsWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.IsWord=True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.IsWord
            if word[i]=='.':
                for child in node.children:
                    if child is not None and dfs(child,i+1):
                        return True
                return False
            index=ord(word[i])-ord('a')
            child=node.children[index]
            if child is None:
                return False
            return dfs(child,i+1)
        return dfs(self.root,0)

