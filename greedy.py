import cs50

while True:
    print("How much change is owed?: ", end="")
    change = cs50.get_float()
    if change > 0:
        break
    else:
        print("enter positive number!")
    
cents = round(change*100)

coins = 0

coins += cents //25
cents %= 25

coins += cents //10
cents %= 10

coins += cents //5
cents %= 5

coins += cents

print(coins)