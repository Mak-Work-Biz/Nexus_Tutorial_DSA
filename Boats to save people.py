class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j = 0, len(people) -1
        people.sort()
        output = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                
                i += 1
                j-=1
                output +=1
            else:
                j-=1
                output += 1
        return output
