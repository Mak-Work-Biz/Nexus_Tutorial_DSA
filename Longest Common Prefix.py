class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_letters = []
        for i in range(len(strs[0])):
            for j in range(len(strs[1])):
                for k in range(len(strs[2])):
                    if strs[0][i] == strs [1][j] == strs[2][k]:
                        common_letters.append(strs[0][i])
        return ''.join(common_letters)
       
