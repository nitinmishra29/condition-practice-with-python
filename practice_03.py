# grade calculator
#------------------------- assign a letter grade based on a student score:A(90-100),B(80-89),C(70-79),D(60-69)F(below 60)


(your_score) = int(input("enter score: "))

if your_score >= 101:
    print("enter correct score")
    exit()
if your_score >= 90:
    grade="A"
elif your_score >= 80:
    grade="B"
elif your_score >= 70:
    grade="C" 
elif your_score >= 60:
    grade="D"
else:
    grade="E"
print(str(grade))
