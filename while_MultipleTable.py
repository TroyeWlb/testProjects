def multiple_table():
    """"hello hello"""
    row = 1  # 行\n换行\t制表符（转意）define函数=def+tap(选中代码正文)
    # col = 1 #列
    while row <= 9:
        col = 1
        while col <= row:
            #    print('%d' % col)
            #    print('*', end='') #col<=row则一直输出*
            print('%d * %d = %d' % (col, row, col * row), end='\t')
            col += 1
            # print('No. %d' % row)
        print('No. %d' % row)
        row += 1

