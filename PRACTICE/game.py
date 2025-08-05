import random

player1 = 0
player2 = 0

snakes = {3:0,99:54,46:6,96:5,50:20,7:5,19:9,32:12,68:39,80:40}
laders = {2:17,13:63,10:98,24:76,33:56,79:84,88:92}


while player1<100 and player2<100:
    p1 = input("[s]top and [c]ontinue: ")
    if p1 == "c":
        p1_turn = random.randint(1,6)
        player1+=p1_turn
        if player1 in snakes :
            player1 = snakes[player1]
            print(f"\n player1 - snake bite - score : {player1}-dice{p1_turn}\n")
        elif player1 in laders:
            player1 = laders[player1]
            print(f"\n player1 - lader - score :{player1}-dice{p1_turn}\n")
            
            
        print(f"\n player1 score:{player1} - dice{p1_turn}\n")
    else:
        print("player2 wins")
        break 
    p2 = input("[s]top and [c]ontinue: ")
    if p1 == "c":
        p2_turn = random.randint(1,6)
        player2+=p2_turn
        print(F"player2 score:{player2} - dice{p2_turn}")
    else:
        print("player1 wins")
        break

    