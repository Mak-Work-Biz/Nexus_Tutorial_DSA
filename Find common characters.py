class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = list(words[0])

        for i in words[1:]:
            output = []
            for j in word:
                if j in i:
                    output.append(j)
                    i = i.replace(j, "", 1)
            word = output
        return word
