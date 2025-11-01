class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        target = Counter(p)
        window = Counter(s[:len(p)-1])

        for i in range (len(p)-1,len(s)):
            curr = s[i]
            window [curr] +=1
            if window == target:
                results.append(i-len(p)+1)
            window[s[i-len(p)+1]] -= 1
            if window [s[i-len(p)+1]]==0:
                del window [s[i-len(p)+1]]
        return results
