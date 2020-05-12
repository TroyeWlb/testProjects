temp = input("数字")
guess = int(temp)
if guess == 8:
    print("yes")
else:
    print("no")

i = 0
while i < 10:
    if i == 3:
        break
    print(i)
    i += 1
print("over")
i = 0
r = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        r += i  # result=result+i
        if i == 80:
            break  # break循环内，计数器前，continue确认循环计数修改，计数器后i+1

    i += 1  # i+1
print("偶数累加 = %d" % r)
