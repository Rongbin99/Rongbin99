print("Pizza Program\n****************")

name = input("What is your name? ")
price = float(input("What is the price for a round pizza? "))
dia = float(input("What is the diameter of the pizza in CM? "))

num = price / dia
rounded = round(num, 3)

print(name, ", your pizza is $", rounded, "per square CM. " )
