class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average=sum(self.scores)/len(self.scores)
        if average>=90 and average<=100:
            return 'O'
        elif average>=80 and average<90:
            return 'E'
        elif average>=70 and average<80:
            return 'A'
        elif average>=55 and average<70:
            return 'P'
        elif average>=40 and average<55:
            return 'D'
        elif average>0 and average<40:
            return 'T'
#redefining the print function to remove the extra spaces
print_object = print
def print(*items_to_print):
    if 'Grade: ' in items_to_print:
        items_to_print = map(str, items_to_print)
        
        print_object(''.join(items_to_print))
    else:
        print_object(*items_to_print)
		
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())