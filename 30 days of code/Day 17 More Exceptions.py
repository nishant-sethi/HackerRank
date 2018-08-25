#Write your code here
class Calculator():
    def power(self,n,p):
        try:
            if(n<0 or p<0):
                raise Exception
            else:
                return n**p
        except Exception:
            return "n and p should be non-negative"