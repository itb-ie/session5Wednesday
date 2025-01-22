from random import choice
drinks = ["gin", "vodka", "wiskey", "rum", "tequila", "absinthe", "sake"]
# print(choice(drinks))
name = input("I am the virtual bartender. What is your name? ")
legal = False
try:
    age = input("What is your age? ")
    age = int(age)
    country = input("What is your country? ")
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
except ValueError:
    print("Don't play games with me")

# outside the except
if legal:
    print("Dear", name, "It's my pleasure to serve you", choice(drinks))
else:
    print("Dear", name, "Unfortunately I can not serve you")