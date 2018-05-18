
import sys

def solve(grades):
    # Complete this function
    new_grades=[]
    for i in grades:
        if(i<38):
            new_grade=i 
        else:
            x=i%5
            if(x<3):
                new_grade=i
            else:
                new_grade=(i/5+1)*5
        new_grades.append(new_grade)
    return new_grades


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))