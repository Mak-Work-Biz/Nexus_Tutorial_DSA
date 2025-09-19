class Solution:
    def interpret(self, command: str) -> str:
        word=[]
        i = 0
        for ch in command:
            while i < len(command):
                if command[i] == 'G':
                    word.append('G')
                    i+=1
                elif command[i] == '(':
                    if command[i+1] == ')':
                        word.append('o')
                        i+=2
                    elif command[i+1:i+4] == 'al)':
                        word.append('al')
                        i+=4
        return ''.join(word)
