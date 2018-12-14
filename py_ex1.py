from Board import Board
from IDS import IDS
from AStar import AStar
from BFS import BFS

def main():

    # reading input file while ignoring empty lines
    with open("input.txt") as f:
        lines = [line.rstrip('\n') for line in open('input.txt')]
    # adding information only
    info = []
    for i in range(len(lines)):
        if lines[i] != '':
            info.append(lines[i])

    algo_type = info[0]
    board_size_str = info[1]
    initial_state_with_dashes = info[2]
    initial_state = initial_state_with_dashes.split("-")

    # create the relevant algorithm
    if algo_type == "1":
        algorithm = IDS()
    elif algo_type == "2":
        algorithm = BFS()
    else:
        algorithm = AStar()

    size = int(board_size_str)
    # creating #board-size empty arrays
    arr = [[] for i in range(int(size))]

    # fill the array with the given values
    j = 0
    for i in range(int(size)):
        for k in range(int(size)):
            arr[i].append(int(initial_state[j]))
            j += 1

    # creating the board instance
    board = Board(arr, size)
    # solve
    algorithm.run(board)

if __name__ == '__main__':
    main()