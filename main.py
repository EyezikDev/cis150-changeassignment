DIVIDER = "\n[]----------------------------------------------------------------[]\n"

coins = [25, 10, 5, 1]
coinsReturn = []
floatingPrice = 0
intPrice = 0

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print(DIVIDER)
print('            Welcome to the Virtual Vending Machine!')
print(f"\n     Stock Start: {quarters} quarters, {dimes} dimes, {nickels}, and {pennies} pennies")
print(DIVIDER)

changeTotal = 0
money = ()
running = True
while running:
    if input("Would you like to purchase an item? y/n > ").upper() == "Y":
        valid = True
        while valid:
            try:
                isZeroOrNeg = True
                while isZeroOrNeg:
                    floatingPrice = float(input("Please enter a purchase price in floating-point form > "))
                    if floatingPrice > float(0):
                        isZeroOrNeg = False
                    elif floatingPrice == float(0):
                        print("Incorrect Format! Can not be 0")
                    elif floatingPrice < float(0):
                        print("Incorrect Format! Can not be negative")
                isZeroOrNeg = True
                while isZeroOrNeg:
                    intPrice = int(input("Please enter a purchase price in integer form > "))
                    if intPrice > 0:
                        isZeroOrNeg = False
                    elif intPrice == float(0):
                        print("Incorrect Format! Can not be 0")
                    elif intPrice < float(0):
                        print("Incorrect Format! Can not be negative")
                    else:
                        print("Incorrect Format! Can not be 0")
                changeTotal = (intPrice - floatingPrice)
                changeTotal = round(changeTotal, 2) * 100
            except ValueError:
                print("Incorrect Format!")
                continue
            else:
                valid = False
        print(DIVIDER)
        print(f"Change difference: {round(changeTotal / 100, 2)}")

        print(DIVIDER)
        print(f"\n     Stock After: {quarters} quarters, {dimes} dimes, {nickels}, and {pennies} pennies")
        print(DIVIDER)
    else:
        running = False
