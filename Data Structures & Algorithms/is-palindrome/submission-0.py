class Solution:
    def isPalindrome(self, s: str) -> bool:
        bob = s.lower()
        bob.strip()
        bob.replace(" ","")
        #no more whitespace, all lowercase
        bob2 = ""

        for ch in bob:
            if ch.isalnum():
                bob2+=ch
        length = len(bob2)
        for i in range(length):
            if (bob2[i]!=bob2[length-1-i]):
                return False

        return True
            

