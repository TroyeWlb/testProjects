import random
player = int(input("yourkey"))
computer = random.randint(1,3)
result = 0
if player < 4:
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):

        print("You Win")
    elif player == computer:
        print(player + computer)
    else:
        print("Let's go")
else:
     while player <= 9:
         print("Hello" * 5)
         player += 1
     if player > 9:
         result += player
         result += 1



