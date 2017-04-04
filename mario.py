import cs50


while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if height > 0 and height < 23:
        break
    else:
        print("enter number between 0 and 23!")

for i in range(height + 1):
        for s in range(height - i):
            print(" ", end="")
        for h in range(i):
            print("#", end="")
        print(" ")



        


        
        