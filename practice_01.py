#classify a person age group: child(<13),teenager(13-19),adult(20-59),senior(60)

user_age=int(input("please enter your age: \n"))
if (user_age<13):
     print('child')
elif (user_age<20):
    print('teenage')
elif (user_age<60):
     print('adult')
else:
     print('senior')
               