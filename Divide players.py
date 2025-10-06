class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j = 0,len(skill)-1
        output = []
        while i <= j:
            output.append((skill[i],skill[j]))
            i+=1
            j-=1
        sum = []
        for i in output[:]:
            sum.append(i[0]+i[1])

        
        summ = 0
        if len(set(sum)) != 1:
            return -1
        else:
            for j in output[:]:
                summ += j[0] * j[1]
            return summ

