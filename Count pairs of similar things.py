class Solution:
    def similarPairs(self, words: List[str]) -> int:
        unique = [set(i) for i in words]

        output = 0
        for i in range(len(unique)):
            for j in range(i+1, len(unique)):
                if unique[i] == unique[j]:
                    output += 1
                        
        return output
