# rock paper scissors
import random
import easygui as g

options = ["rock","papper","scissors"]
run = True
# cpu_win = 0
# player_win = 0
while run:

# for x in range(5):
    cpu_choice = random.choice(options)

    player = g.buttonbox("Please choose one", title="RPS game.", choices=(options))

    if player==cpu_choice:
        g.msgbox(f"It is a draw, both have selected {player}")
    elif player == options[0] and cpu_choice == options[2] or player==options[1] and cpu_choice==options[0] or player[2] and cpu_choice==options[1]:
        g.msgbox(f"Yaaay, you won, with your {player}")
        #player_win+=1
    else:
        g.msgbox(f"You lose!! Cpu won with {cpu_choice}")
        #cpu_win+=1
    #run = g.ynbox("Do you want to play again?")
