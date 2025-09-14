class Solution:
    def isPalindrome(self, x: int) -> bool:
        characters = []
        for i in str(x):
            characters.append(i)
        if characters == characters[::-1]:
            return True
        else:
            return False
