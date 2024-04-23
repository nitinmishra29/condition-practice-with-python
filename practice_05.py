# coffe  cutimaization
# customize a coffee order small , medium, and large with option for extra sort of espresso
coffee_size = input("enter a size small medium or large: ")
extra_shot= input("enter true or false: ")

if extra_shot:
    coffee= coffee_size + " coffee with extra shot"
else:
    coffee= coffee_size + " coffee"
print ("order:",coffee)


