#movie ticket pricing 
#-----------------movie ticket price based on age: $12 for adults(18 or over),$8  for childeren .everone get $2 discount on wednesday


age= int(input("eneter your age: "))
day=str(input("write down a day: "))

price=12 if age>=18 else 8
int(price)
if day=="wednesday":
   # price= price-2
    price -=2
print("ticket price is for you $", price)


