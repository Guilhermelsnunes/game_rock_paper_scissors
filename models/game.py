class Game():

    def Evaluate ( player_1, player_2 ):
        if player_1.choice == player_2.choice:
            return None, None
        elif ( player_1.choice == "rock" and player_2.choice == "scissors" ) or \
            ( player_1.choice == "scissors" and player_2.choice == "paper") or \
            ( player_1.choice == "paper" and player_2.choice =="rock"):
            return player_1, player_2
        else:
            return player_2, player_1
