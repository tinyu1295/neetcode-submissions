class Solution:
    def validChecker(opChar, clChar):
        if opChar == "(" and clChar == ")":
            return True
        elif opChar == "{" and clChar == "}":
            return True
        elif opChar == "[" and clChar == "]":
            return True
        else:
            return False
        

    def isValid(self, s: str) -> bool:
        storeChar = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in closeToOpen:
                if storeChar and storeChar[-1] == closeToOpen[i]:
                    storeChar.pop()
                else:
                    return False
            else:
                storeChar.append(i)
        
        return True if not storeChar else False





