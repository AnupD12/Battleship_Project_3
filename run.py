from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        self.hits = []

    def print(self):
        for row in self.board:
            print("".join(row)) 

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X" 

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            self.hits.append((x, y))
            print("Hit")
            return "Hit"

        else:
            print("Miss")
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"
        print(self.ships)


def random_point(size):
    """
    Function to create a random number based on the size of the board
    """
    # print(randint(0, size - 1))
    return randint(0, size - 1)


def populate_board(board):
    """
    """
    # size = int(input("No. of Rows and Columns = "))
    # num_ships = int(input("No. of Ships = "))
 
    while len(board.ships) < board.num_ships:
        point_x = random_point(board.size)
        point_y = random_point(board.size)
        board.add_ship(point_x, point_y)

    print(f"{board.type}'s board")
    board.print()      


def make_guess(board):
    """
    """
    if board.guesses != board.ships and board.type == "computer":
        guess_x = int(input("Guess x point = "))
        guess_y = int(input("Guess y point = "))
        board.guess(guess_x, guess_y)
        populate_board(board)
    else:
        guess_x1 = random_point(board.size)
        guess_y1 = random_point(board.size)
        if (guess_x1, guess_y1) not in board.guesses:
            board.guess(guess_x1, guess_y1)
            populate_board(board)


def play_game(computer_game, player_game):
    """ 
    """
    while len(computer_game.hits) < computer_game.num_ships:
        make_guess(computer_game)
        make_guess(player_game)
        if len(computer_game.hits) == computer_game.num_ships:
            print("player wins")
        elif len(player_game.hits) == player_game.num_ships:
            print("computer wins")
    
    
def new_game():
    """
    
    """

    size = int(input("No. of Rows and Columns = "))
    num_ships = int(input("No. of Ships = ")) 

    print("-"*15) 
    print(f"Board size: {size}. Number of ships: {num_ships}")
    computer_game = Board(size, num_ships, "computer", type="computer")
    player_game = Board(size, num_ships, "player", type="player")
    populate_board(computer_game)
    print("-"*15)
    populate_board(player_game)
    play_game(computer_game, player_game)
    
        
new_game()


