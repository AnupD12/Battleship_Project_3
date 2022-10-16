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

    def print(self):
        for row in self.board:
            print("".join(row)) 

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X" 

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"

        else:
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
    """
    print(randint(0, size - 1))
    return randint(0, size - 1)


def populate_board(size):
    """
    """
    point_x = random_point(size)
    point_y = random_point(size)

def new_game():
    """
    
    """

    # size = int(input("No. of row and Columns = "))
    size = 5
    # num_ships = int(input("no. of ships = "))
    num_ships = 2 
    print("-"*15) 
    print(f"Board size: {size}. Number of ships: {num_ships}")
    computer_game = Board(size, num_ships, "computer", type="computer")
    computer_game.print()
    # point_x = random_point(size)
    # point_y = random_point(size)
    # new_ship = computer_game.add_ship(point_x, point_y)  
    populate_board(size)
    
    

new_game()


