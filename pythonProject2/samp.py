from random import randint

Sec = int(randint(1,9))
print(Sec)
count = 1

while (count!=4):
    print("hello world")
    no = int(input("enter a num: "))
    if(Sec != no):
        count = count + 1
        print("Another chance")
    else:
        print("better luck next time")

print("correct you won jackpot")













