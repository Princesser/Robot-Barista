#Let's start a coffee shop and build Robot barisata



print("Hello, welcome to princess coffee!!")

Name = input("What's your name?\n")


print("Hello " + Name + ", thank you so much for coming in today.")
  
Menu = "Black coffee, Cuppuccino, Expresso, latte, Doppio "

print(Name + ", what would you love from our menu today? " + "Here is what we are serving. \n" + Menu)

Order = input()

Price = 10

Quantity = input("How many coffe would you like?\n")

Total = Price * int(Quantity)

print("Thank you. Your total is: $" + str(Total))

print("Sounds good " + Name + ", we'll have your "  + Quantity + " " + Order + " ready for you in a monent.")