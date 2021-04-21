from random import randint
d_max=0
d_min=0
i=0
ram =randint(2,200)
print("Choose Number Between 2 to 200!")
while True:
    while i<5 :
        num = int(input("enter your number :"))
        print(F"your remaing chance:{(4-i)}")
        if (num < 0):
            print("plz chose any number:")
        elif (num == ram):
            print("you win:")
            break
        elif (ram>num):
            d_min = ram - num
            if (d_min > 5):
                print("Too Low:")
            elif (d_min <= 5):
                print(" Low:")
        elif (num>ram):
            d_max = num - ram
            if (d_max > 5):
                print("Too High:")
            elif (d_max <= 5):
                print(" High:")

        if i==4:
            print("you loser")
        i=i+1
    i=0
    ram = randint(2, 200)
    print("---------------Next chance-----------------")
