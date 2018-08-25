class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result=1
        for i in range(2,n+1):
            if n%i==0:
              
                result+=i
        return result