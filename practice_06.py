# password strength checker
#------check if password is weak(6 char) medium(6-10 char) or strong (10+ char)

password = input("enter password: ")

if len(password) <6:
    strength = "weak"
elif len(password) <=10:
    strength =" medium"
else:
    strength = "strong"

print("strength: ",strength)