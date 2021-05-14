class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def f(c):
            return ord(c) - 97
    
        ct_p, ct_s = [0] * 26, [0] * 26
        for c in p:
            ct_p[f(c)] += 1
        l = len(p)
        for c in s[:l - 1]:
            ct_s[f(c)] += 1
        res = []
        for i, c in enumerate(s[l - 1:]):
            ct_s[f(c)] += 1
            if ct_s == ct_p:
                res.append(i)
            ct_s[f(s[i])] -= 1
        return res
