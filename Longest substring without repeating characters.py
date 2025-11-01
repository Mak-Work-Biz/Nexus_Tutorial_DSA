class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0

        for i in range(len(s)):
            result = []
            for j in range(i, len(s)):
                if s[j] not in result:
                    result.append(s[j])
                else:
                    break
            max_len = max(max_len, len(result))

        return max_len
