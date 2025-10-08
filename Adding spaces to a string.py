class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        i=0
        for j,ch in enumerate(s):
            if i < len(spaces) and j == spaces[i]:
                output.append(' ')
                i +=1
            output.append(ch)
        return ''.join(output)
            
