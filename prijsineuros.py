#! bin/python3
print("Deze tool berekend btw")
prijs = input("Wat is de prijs in euros? ")
btw = int(prijs) /100 * 21
print("De btw hierop is " + str(btw))

