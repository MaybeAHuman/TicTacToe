action = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]

BOARD = f"- - - - - - -\n| {action[0]} | {action[1]} | {action[2]} |\n- - - - - - -\n| {action[3]} | {action[4]} | {action[5]} |\n- - - - - - -\n| {action[6]} | {action[7]} | {action[8]} |\n- - - - - - -"

def gamePlay(player1, player2, action):    
    action[int(player1)] = "O"
    action[int(player2)] = "X"

    return action

print(BOARD)

while True:
    player1 = input("Player 1(O) [0-8]: ")

    player2 = input("Player 2(X) [0-8]: ")
    
    action = gamePlay(player1, player2, action)
    print(BOARD)
