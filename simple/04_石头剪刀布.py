player = int(input("请输入您要出的拳（石头1  剪刀2  布3）："))
computer = 1

if player == 1:
    print("玩家选择的是石头")
elif player == 2:
    print("玩家选择的是剪刀")
elif player == 3:
    print("玩家选择的是布")
else:
    print("数字不合理。")

print("电脑出的是 %d " % computer)

if ( player == 1 and computer == 3 ) or ( player == 2 and computer == 1 ) or ( player == 3 and computer == 2 ):
    print("你输了")
elif player == computer:
    print("平局")
else:
    print("你赢了")

