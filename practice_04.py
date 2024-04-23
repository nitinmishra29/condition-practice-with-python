
# determine the fruit is ripe unripe or overripe based on its color banana :green unripe,yellow ripe, brown overipe
#--------------
fruit = str(input("enter the fruit type : "))
color= str(input("Enter the fruit color : "))

if fruit  =="banana":
    if color=="green":
        print("unripe")
    elif color=="yellow":
        print("ripe")
    elif color=="brown":
        print("overripe")

else:
    print("data not available")