class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        max_f = 0
        best = 0
        for j, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_f = max(max_f, count[ch])
            while (j - i + 1) - max_f > k:
                count[s[i]] -= 1
                i += 1
            best = max(best, j - i + 1)
        return best