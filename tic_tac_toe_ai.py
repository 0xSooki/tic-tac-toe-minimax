import math
import random

class Player(object):
    def __init__(self, marker, isMaximizing):
        self.score = 0
        self.marker = marker
        self.isMaximizing = isMaximizing
    
    def win(self):
        self.score += 1
    
    def lose(self):
        if self.score <= 0:
            self.score = 0
        else:
            self.score -= 1

    def show_score(self):
        print(f"{self.name} has {self.score} points")

ai = Player("X", True)
human = Player("O", False)

class playingField(object):
    def __init__(self):
        self.depth = 0
        self.scores = {
            "X": 1,
            "O": -1,
            "tie": 0
        }
        self.field = [
            [" ", " ", " "],
            [" ", "O", " "],
            [" ", " ", " "]
        ]
    
    def show_board(self):
        blankBoard=f"""
    ___________________
    |     |     |     |
    |  {self.field[0][0]}  |  {self.field[0][1]}  |  {self.field[0][2]}  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  {self.field[1][0]}  |  {self.field[1][1]}  |  {self.field[1][2]}  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  {self.field[2][0]}  |  {self.field[2][1]}  |  {self.field[2][2]}  |
    |     |     |     |
    |-----------------|
    """
        print(blankBoard)

    def board_is_full(self):
    #check if the board is full
        for row in self.field:
            if " " in row:
                return False
                break
        else:
            return True

    def set_marker(self, pos, player):
        self.field[pos[0]][pos[1]] = player

    def convert_to_coord(self, move):
        y = int(move/3)
        x = move%3
        if x != 0:
            x -=1
        else:
            x = 2
            y -=1
        return y, x

    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.field[r][c] = " "

    def space_check(self, pos):
        return self.field[pos[0]][pos[1]] == " "
            
    def win_check(self):
        if self.board_is_full():
            return "tie"
        elif (self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[1][1] in "XO") or (self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[1][1] in "XO"):
            return self.field[1][1]
        for r in range(3):
            if (self.field[r][0] == self.field[r][1] == self.field[r][2] and self.field[r][0] in "XO"):
                return self.field[r][0]

            elif (self.field[0][r] == self.field[1][r] == self.field[2][r] and self.field[0][r] in "XO"):
                return self.field[0][r]
        else:
            return False

    def minimax(self, depth, player):

        if player.isMaximizing:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, math.inf]
        
        result = self.win_check()
        if result != False:
            score = self.scores[result]
            return [-1, -1, score]

        for x in range(3):
            for y in range(3):
                if self.field[x][y] == " ":
                    self.field[x][y] = player.marker
                    if player.isMaximizing:
                        score = self.minimax(depth+1, human)
                    else:
                        score = self.minimax(depth+1, ai)
                    self.field[x][y] = " "
                    score[0], score[1] = x, y

                    if player.isMaximizing:
                        if score[-1] > best[-1]:
                            best = score
                    else:
                        if score[-1] < best[-1]:
                            best = score
        return best

def main():
    playing = True
    game_on = True

    board = playingField()
    pos = 0

    print("1|2|3")
    print("4|5|6")
    print("7|8|9")

    while playing:
        board.reset_board()

        game_on = True

        while game_on:
            board.show_board()
            move = board.minimax(board.depth, ai)
            board.field[move[0]][move[1]] = "X"
            win = board.win_check()
            #validate user input
            while True and win == False:
                
                board.show_board()
                pos = input("Declare your move: ")
                try:
                    pos = int(pos)
                except ValueError:
                    print("Enter a valid number!")
                    continue
                if 1<=pos<=9:
                    if board.space_check(board.convert_to_coord(pos)):
                        break
                    print("Target already occupied!")
                else:
                    print("Invalid target!")

            board.set_marker(board.convert_to_coord(pos), human.marker)

            if win != False:

                if win == "tie":
                    print("Tie!")
                    game_on = False

                elif win == "X":
                    print("The ai won!")
                    ai.score += 1
                    game_on = False
                else:
                    print("You won")
                    human.score += 1
                    game_on = False

            if game_on == False:
                board.show_board()
                print("--------------------------")
                print(f"ai:{ai.score}/you:{human.score}")
                print("--------------------------")
                if str(input("Do you want to play again? [Y/N] ")).lower() == "y":
                    playing = True
                    break
                else:
                    playing = False
                    break

if __name__ == "__main__":
    main()

