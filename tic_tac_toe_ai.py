import math
import random

class Player(object):
    def __init__(self, name, score, marker):
        self.name = name
        self.score = score
        self.marker = marker
        self.depth = 0
    
    def win(self):
        self.score += 1
    
    def lose(self):
        if self.score <= 0:
            self.score = 0
        else:
            self.score -= 1

    def show_score(self):
        print(f"{self.name} has {self.score} points")

class playingField(object):
    def __init__(self):
        self.scores = {
            "X": 1,
            "O": -1,
            "tie": 0
        }
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
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
        if board_is_full():
            return "tie"
        elif (self.field[0][0] == self.field[1][1] == self.field[2][2]) or (self.field[0][2] == self.field[1][1] == self.field[2][0]):
            return self.field[1][1]
        for r in range(3):
            if (self.field[r][0] == self.field[r][1] == self.field[r][2] == "O" or "X"):
                return self.field[r][0]

            elif (self.field[0][r] == self.field[1][r] == self.field[2][r] == "O" or "X"):
                return self.field[0][r]
        else:
            return False

    def minimax(self, depth, board, maximizing):
        result = win_check()
        if result != False:
            score = scores[result]
            return score

        if maximising:
            bestScore = -math.inf
            for r in board:
                for c in r:
                    if board[r][c] == " ":
                        board[r][c] = ai.marker
                        score = minimax(board, depth+=1, false)
                        board[r][c] = " "
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = math.inf
            for r in board:
                for c in r:
                    if board[r][c] = " ":
                        board[r][c] = player2.marker
                        score = minimax(board, depth+=1, false)
                        board[r][c] = " "
                        bestScore = min(score, bestScore)

    def bestMove(self):
        best_score = -math.inf
        for r in board:
            for c in r:
                if board[r][c] = " ":
                    board[r][c] = ai
                    score = minimax(0 ,board, true)
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
                    board[r][c] = " "
        self.board[best_move[0], best_move[1]]
    
def main():
    playing = True
    game_on = True

    player1 = Player(str(input("Enter the name of the first player: ")), 0, "X")
    player2 = Player(str(input("Enter the name of the second player: ")), 0, "O")

    board = playingField()
    pos = 0

    print("1|2|3")
    print("4|5|6")
    print("7|8|9")

    while playing:
        current_player = player1

        board.reset_board()

        game_on = True

        while game_on:
            board.show_board()

            #validate user input
            while True:
                pos = input(f"{current_player.name} declare your move: ")
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

            board.set_marker(board.convert_to_coord(pos), current_player.marker)

            win = board.win_check()

            if win != False:

                if win == "tie":
                    print("Tie!")
                    game_on = False

                else:
                    print(f"{current_player.name} won!")
                    current_player.win()
                    game_on = False

            if game_on == False:
                board.show_board()
                print("--------------------------")
                print(f"{player1.name}:{player1.score}/{player2.name}:{player2.score}")
                print("--------------------------")
                if str(input("Do you want to play again? [Y/N] ")).lower() == "y":
                    playing = True
                    break
                else:
                    playing = False
                    break

            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

if __name__ == "__main__":
    main()

