class Solution:
    def freqAlphabets(self, s: str) -> str:
        string_new = ''
        i=0
        while i < len(s):
            if s[i:i+3] in [str(x) + '#' for x in range(10,27)]:
                num = int(s[i:i+2])
                string_new += chr(ord('a') + num -1)
                i=i+3
                
            elif s[i] in '123456789':
                num = int(s[i])
                string_new += chr(ord('a') + num -1)
                i=i+1
        return string_new
                
