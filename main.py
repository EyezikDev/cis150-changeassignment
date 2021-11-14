import os

DIVIDER = "\n[]----------------------------------------------------------------[]\n"
QUARTER = 25
DIME = 10
NICKLE = 5
PENNIE = 1

floatingPrice = 0
intPrice = 0
changeTotal = 0
quarters = 10
dimes = 10
nickels = 10
pennies = 10
running = True
valid = True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(DIVIDER)
print('            Welcome to the Virtual Vending Machine!')
print(f"\n     Stock Start: {quarters} quarters, {dimes} dimes, {nickels}, and {pennies} pennies")
print(DIVIDER)

while running:
    userInput = input("Would you like to purchase an item? y/n > ").upper()
    if userInput == "Y":
        while valid:
            try:
                isNotIncorrect = True
                while isNotIncorrect:
                    floatingPrice = int(float(input("Please enter a purchase price in floating-point form > ")) * 100)
                    if floatingPrice > 0:
                        isNotIncorrect = False
                    elif floatingPrice == 0:
                        print("Incorrect Format! Can not be 0")
                    elif floatingPrice < 0:
                        print("Incorrect Format! Can not be negative")
                isNotIncorrect = True
                while isNotIncorrect:
                    intPrice = int(input("Please enter a purchase price in integer form > ")) * 100
                    if intPrice > 0:
                        isNotIncorrect = False
                    elif intPrice == 0:
                        print("Incorrect Format! Can not be 0")
                    elif intPrice < 0:
                        print("Incorrect Format! Can not be negative")
                    else:
                        print("Incorrect Format! Can not be 0")
                changeTotal = intPrice - floatingPrice
            except ValueError:
                print("Incorrect Format!")
                continue
            else:
                valid = False
        print(DIVIDER)
        print(f"Change difference: {round(changeTotal / 100, 2)}")
        coinsUsed = 0
        quartersUsed = 0
        dimesUsed = 0
        nickelsUsed = 0
        penniesUsed = 0
        while changeTotal >= QUARTER and quarters > 0:
            quartersUsed += 1
            quarters -= 1
            changeTotal -= QUARTER
            coinsUsed += 1
        print(f"Quarter(s)       > {quartersUsed}")
        while changeTotal >= DIME and dimes > 0:
            dimesUsed += 1
            dimes -= 1
            changeTotal -= DIME
            coinsUsed += 1
        print(f"Dime(s)          > {dimesUsed}")
        while changeTotal >= NICKLE and nickels > 0:
            nickelsUsed += 1
            nickels -= 1
            changeTotal -= NICKLE
            coinsUsed += 1
        print(f"Nickle(s)        > {nickelsUsed}")
        while changeTotal > PENNIE and pennies > 0:
            penniesUsed += 1
            pennies -= 1
            changeTotal -= PENNIE
            coinsUsed += 1
        print(f"Pennie(s)        > {penniesUsed}")
        print(f"Coin(s)          > {coinsUsed}")
        coinTracker = quarters + nickels + dimes + pennies
        print(DIVIDER)
        if coinTracker == 0:
            print(f"     Stock Is Empty, Goodbye.")
            running = False
        else:
            print(f"     Stock After: {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies")
        print(DIVIDER)
    elif userInput == "N":
        running = False
    else:
        continue
