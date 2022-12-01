from itertools import takewhile
FILENAME = '04-input.txt'

def read_boards(board_sequence):
    """
    Read the text input of boards. Return a list of lists: The rows and columns of the initial grid.
    We're going to remove numbers from the board whenever they get called.
    """
    while (board := list(takewhile(lambda l: len(l) > 0, board_sequence))):
        board = [ [ int(cell) for cell in line.split(' ') if cell ] for line in board ]
        # Add a row for each of the columns
        board.extend([ [row[i] for row in board] for i in range(len(board)) ])
        yield board

def remove_number(reveal, board):
    """
    Remove the "reveal" value from the board wherever it appears
    """
    return [[ cell for cell in row if cell != reveal ] for row in board ]

def is_bingo(board):
    """
    If any row is of 0 length, all its numbers got removed after being called.
    Bingo!
    """
    return any(len(row) == 0 for row in board)

def board_sum(board):
    """
    Work out the sum of the uncalled numbers.
    Values are counted twice in board -- once in the rows, once in the columns.
    We internally divide the sum by two so each number is counted once instead of twice.
    """
    return int(sum(cell for row in board for cell in row) / 2)

def play_01(reveals, boards):
    """
    Breadth first search. Loop through every reveal, within which play every board.
    """
    for reveal in reveals:
        for i in range(len(boards)):
            boards[i] = remove_number(reveal, boards[i])
            if is_bingo(boards[i]):
                return board_sum(boards[i]) * reveal

def play_02(reveals, boards):
    """
    Breadth first search with caveat.
    Loop through every reveal and every board. 
    Detect bingos for the last board but ignore the rest
    """
    for reveal in reveals:
        boards = [ remove_number(reveal, board) for board in boards if not is_bingo(board) ]
        if len(boards) == 1 and is_bingo(boards[0]):
            return board_sum(boards[0]) * reveal

with open(FILENAME) as bingo:
    reveals = [ int(n) for n in next(bingo).split(',') ]
    # skip the blank line
    next(bingo)
    boards = list(read_boards(line.strip() for line in bingo))
    print(play_02(reveals, boards))
