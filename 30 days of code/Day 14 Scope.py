	# Add your code here
        self.maximumDifference=None
    def computeDifference(self):
        a=sorted(self.__elements)
        x=abs(a[0]-a[len(a)-1])
        self.maximumDifference=x