class Solution:
    def isMatch(self, x, y) -> bool:
        if(x=="[" and y=="]"):
            return True
        elif(x=="{" and y=="}"):
            return True
        elif(x=="(" and y==")"):
            return True
        else:
            return False
            
    def isValid(self, s: str) -> bool:
        e = []
        for i in s:
            if(len(e)>0 and self.isMatch(e[len(e)-1],i)==True):
                e.pop()
            else:
                e.append(i)
        
        return len(e)==0


        