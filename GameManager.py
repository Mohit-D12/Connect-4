from Frame import Frame
from MC200 import MC200
from MC40 import MC40
from time import time

class GameManager:
    
    def __init__(self):
        self.frame = Frame()
        print("Connect 4!")
        self.display_board()
    
    def player_move(self):
        move = int(input())
        
        try:
            return self.play_move(move)
        except:
            print("Invalid Move!")
            self.player_move()
    
    def MC200_move(self):
        move = MC200.get_move(self.frame)
        return self.play_move(move)
    
    def MC40_move(self):
        move = MC40.get_move(self.frame)
        return self.play_move(move)
    
    def play_move(self, move):
        self.print_move(move)
        self.frame = self.frame.play_move(move)
        return self.get_game_status()

    def print_move(self, move):
        print("Player", self.frame.get_player(), "plays", move)
        
    def get_game_status(self):
        self.display_board()
        return self.is_game_ended()
    
    def is_game_ended(self):
        return self.is_game_won() or self.is_board_full()
        
    def is_board_full(self):
        if self.frame.is_ended():
            print("DRAW")
            return True
        return False
    
    def is_game_won(self):
        winner = self.frame.get_winner()
        
        if winner > 0:
            print(winner, "Won")
            return True
        
        return False

    def display_board(self):
        self.frame.print_frame() 
        
