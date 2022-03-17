import copy
import random

class Frame:
    
    def __init__(self, frame = None, rows = 6, columns = 5):
        if frame == None:
            frame = self.generate_empty_frame(rows, columns)
        self.frame = frame
        self.player = self.get_player()
        self.max_rows = len(frame)
        self.max_columns = len(frame[0])
    
    def generate_empty_frame(self, rows, columns):
        frame = []
        
        for row in range(rows):
            frame.append([0]*columns)
        
        return frame

    def print_frame(self):
        for row in self.frame:
            for cell in row:
                print(cell, end="  ")
            print()
        print() 
           
    def unroll_frame(self, frame = None):
        if frame == None:
            frame = self.frame
        unrolled_frame = ""
        for row in frame:
            for cell in row:
                unrolled_frame += str(cell)
        
        for index in range(len(unrolled_frame)):
            if unrolled_frame[index] == '0':
                index += 1
            else:
                break
        
        if index == len(unrolled_frame):
            return '0'
        
        return unrolled_frame[index:]
           
    def get_player(self):
        p1 = p2 = 0
        for row in self.frame:
            p1 += row.count(1)
            p2 += row.count(2)
        
        if p1 == p2:
            return 1
        if p1 == p2 + 1:
            return 2
        return -1
        
    def get_valid_moves(self):
        valid_moves = []
        
        for column in range(self.max_columns):
            if self.frame[0][column] == 0:
                valid_moves.append(column+1)
        
        return valid_moves

    def get_random_move(self):
        valid_moves = self.get_valid_moves()
        
        if len(valid_moves):
            return random.choice(valid_moves)
        
        return -1
    
    def play_move(self, move):
        next_state = copy.deepcopy(self)
        move -= 1
        
        for row in range(self.max_rows - 1, -1, -1):
            if self.frame[row][move] == 0:
                next_state.frame[row][move] = self.player
                if self.player == 1:
                    next_state.player = 2
                else:
                    next_state.player = 1
                return next_state
        
        return None

    def is_ended(self):
        for cell in self.frame[0]:
            if cell == 0:
                return False
        return True
    
    def get_winner(self):
        
        #row wise
        for row in self.frame:
            count = 1
            prev = 0
            for cell in row:
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell

        #column wise
        for column in range(self.max_columns):
            count = 1
            prev = 0
            for row in range(self.max_rows):
                cell = self.frame[row][column]
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell
        
        #main diagonal directional diagnals
        for row_start in range(self.max_rows):
            row = row_start
            column = 0
            count = 1
            prev = 0
            while row >= 0 and column < self.max_columns:
                cell = self.frame[row][column]
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell
                row -= 1
                column += 1
        
        for column_start in range(1, self.max_columns):
            row = self.max_rows - 1
            column = column_start
            count = 1
            prev = 0
            while row >= 0 and column < self.max_columns:
                cell = self.frame[row][column]
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell
                row -= 1
                column += 1
                
        #secondary diagonal directional diagnals
        for row_start in range(self.max_rows):
            row = row_start
            column = 0
            count = 1
            prev = 0
            while row < self.max_rows and column < self.max_columns:
                cell = self.frame[row][column]
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell
                row += 1
                column += 1
        
        for column_start in range(1, self.max_columns):
            row = 0
            column = column_start
            count = 1
            prev = 0
            while row < self.max_rows and column < self.max_columns:
                cell = self.frame[row][column]
                if cell != 0 and cell == prev:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    count = 1
                prev = cell
                row += 1
                column += 1
        
        #if no 4-in-a-row
        return 0