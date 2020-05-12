# price = float(input("价格"))
# weight = float(input("重量"))
# total = price * weight
# print("合计 %.02f元 " % total)
# name = input("name")
# print("我的名字叫 %s，请多多关照" % name)
# student_no = int(input("No."))
# print("我的学号是 %09d" % student_no)

# scale = float(input("age"))
# if scale >= 18:
#     print("welcome")
# else:
#     print("go away")
# print(1+2)

# age = int(input("age"))
# if age <= 18:
#     print("请叫家长")
#     if age == 17:
#         print("请明年再来")
#     elif age == 16:
#         print("请后年再来")
#     elif age <= 15:
#         print("回家去吧")
# else:
#     hight = int(input("请输入身高 "))
#     if hight > 160:
#         print("来吧")
#     else:
#         print("你太高了，有 %d 公分高" % hight)

is_employee = True
if not is_employee:
    print("go away")
else:
    nummber = input("No. ")
    if len(nummber) == 4:
        if nummber[0] == "1":
            print("请去一楼")
        elif nummber[0] == "2":
            print("请去二楼")
        elif nummber[0] == "3":
            print("请去三楼")
        else:
            print("go away")
    else:
        print("go away !")

