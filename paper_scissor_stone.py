#這是剪刀石頭布的遊戲

from optparse import Option
import random

player = None #放玩家出的拳種
computer = None #放電腦出的拳種
option = ("剪刀","石頭","布")                                       # tuple 運行速度快也不用修改。
running = True                                                      #確保連續運行

while running:# 其實就是TRUE 一直運行
    player = input("請輸入剪刀、石頭、布:")
    while player not in option :                                    #如果沒有出三種之一的拳種:
        player = input("輸入錯誤:請輸入剪刀、石頭、布:")            #請玩家重新打一次，避免玩家亂打。
    computer = random.choice(option)                        #從option內隨機選出一種拳。
    print(f"玩家出:{player}，電腦出:{computer}")
    
    
    if  player == computer:                     #接下來是遊戲規則，列出玩家獲勝的部分。
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("玩家獲勝")
    
    elif player == "石頭" and computer == "剪刀":
        print("玩家獲勝")
    
    elif player == "布" and computer == "石頭":
        print("玩家獲勝")
    else:                                       #其他狀況電腦獲勝
        print("電腦獲勝")
    
    play_again = input("你要再玩一次嗎?(y/n)?").lower()  #結束遊戲的條件
    if  play_again == "n":
        break

print("謝謝，遊戲結束")



