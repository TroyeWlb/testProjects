s = 0
i = 0
while i <= 100:
    if i % 2 == 1:
        print(i)
        s += i
        if s == 2116:
            break
    i += 1
    print('sum = %d' % s)
