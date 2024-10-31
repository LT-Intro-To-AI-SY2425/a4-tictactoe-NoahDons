# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:

    def __init__(self, board = []):
        self.board = ["*","*","*","*","*","*","*","*","*"]

    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __str__(self) -> str:
        board = ""
        
        board += f"{self.board[0]} {self.board[1]} {self.board[2]} \n"
        board += f"{self.board[3]} {self.board[4]} {self.board[5]} \n"
        board += f"{self.board[6]} {self.board[7]} {self.board[8]} \n"
        return board
    
    def make_move(self, player, pos):
        if pos >= 9 or pos <=-1:
            return False
        
        if self.board[pos] == "*":
            self.board[pos] = player
            return True
        elif self.board[pos] == "O" or self.board[pos] == "X":
            return False
        

    def has_won(self, player):
        won = False
        if self.board[0] == player and self.board[1] == player and self.board[2] == player:
            won = True
        if self.board[3] == player and self.board[4] == player and self.board[5] == player:
            won = True
        if self.board[6] == player and self.board[7] == player and self.board[8] == player:
            won = True

        if self.board[0] == player and self.board[3] == player and self.board[6] == player:
            won = True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            won = True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            won = True

        if self.board[0] == player and self.board[4] == player and self.board[8] == player:
            won = True
        if self.board[2] == player and self.board[4] == player and self.board[6] == player:
            won = True
        return won

    def game_over(self):
        if self.has_won("X"):
            return True
        elif self.has_won("O"):
            return True
        if self.board[0] == "*" and not self.board[0] == "*" and not self.board[1] == "*" and not self.board[2] == "*" and not self.board[3] == "*" and not self.board[4] == "*" and not self.board[5] == "*" and not self.board[6] == "*" and self.board[7] == "*" and not self.board[8] == "*":
            return True
        
        return False
        
    def clear(self):
        for i in range(0, 9):
            self.board[i] = "*"

        


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    play_tic_tac_toe()

    
    brd.make_move("X", 8)
    brd.make_move("O", 7)
    

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() 
    print(brd)== True

    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
