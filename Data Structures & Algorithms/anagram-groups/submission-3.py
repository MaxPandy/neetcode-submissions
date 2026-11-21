from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                index=ord(char)-ord("a")
                count[index]+=1
            words[tuple(count)].append(word)
        return list(words.values())
