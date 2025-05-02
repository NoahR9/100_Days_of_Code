print("Welcome to the tip calculator")
bill = float(input("How much was the bill?\n"))
people = int(input("How many people are splitting the bill?\n"))
tip = int(input("What percent tip would you like to leave? 10,12,15, or 20 are common!\n"))

total = (bill * ((tip /100)+1))/ people


print(round(total,2))


