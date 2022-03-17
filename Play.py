from GameManager import GameManager       

def player_vs_MCX():
    
    print("Choose Player: 1 or 2")
    player_turn = int(input())

    game = GameManager()

    if player_turn == 1:
        game.player_move()
    
    while True:
        if game.MC200_move() or game.player_move():
            return
    
def MCX_vs_MCX():
    game = GameManager()
    while True:
        if game.MC200_move() or game.MC40_move():
            return

if __name__ == "__main__":
    
    while(True):
        print("Enter game mode:")
        print("1. MC200 vs MC40")
        print("2. player vs MC200")

        mode = int(input())

        if mode == 1:
            MCX_vs_MCX()
        elif mode == 2:
            player_vs_MCX()
        else:
            print("Incorrect Mode Selection!")
        
        print("Do you want to continue? (Y/N)")
        choice = input()

        if(choice != 'y' and choice != 'Y'):
            break