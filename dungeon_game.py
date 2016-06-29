import random
import os

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)
    if monster == door:
        get_locations()
    if monster == start:
        get_locations()
    if start == door:
        get_locations()
    print("Monster={} Door={} Start={}".format(monster, door, start))
    return monster, door, start


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        y -= 1
    elif move == "RIGHT":
        y += 1
    elif move == "DOWN":
        x += 1
    else:
        x -= 1

    player = x, y
    return player

def draw_map(player):
    print(' _ _ _')
    tile ='|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end="")
            else:
                print(tile.format('_'), end="")
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))




def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[0] == 0:
        del MOVES[2]
    if player[0] == 2:
        del MOVES[3]
    if player[1] == 0:
        del MOVES[0]
    if player[1] == 2:
        del MOVES[1]
    return MOVES

monster, door, player = get_locations()
total_move = 0

print("Welcome to the dungeon!")

while True:

    print("You're currently in room {}".format(player))  # fill in with player position
    print("You can move {}".format(get_moves(player))) # fill in with available moves
    print("Enter QUIT to quit")
    draw_map(player)
    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in get_moves(player):
        total_move += 1
        player = move_player(player, move)
    else:
        print ("You can't move {}.".format(move))

    if player == door:
        print("You win!!!!!")
        exit()

    if player == monster:
        print("You got eaten by the monster!!!!")
        exit()

