class Solution:
    def isValid(self, s: str) -> bool:
        bob = "({["
        bob2 = ")}]"
        stack = []
        for i in s:
            if i in bob:
                stack.append(i)
            if i in bob2:
                if not stack:
                    return False
                temp = stack.pop()
                ind = bob2.find(i)
                ind2 = bob.find(temp)
                if (ind != ind2):
                    return False

        if (len(stack)>0):
            return False
        return True



        