from typing import List

""" Hey Darius! great work, really like that we are collaborating in person too :D!"""


board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

surrounding_cells = [
        [0,1], #above
        [0,-1], #below
        [-1,0], #left
        [1,0] #right
    ]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced (.)
        new (str): Value that replaces the old (~)
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

        # Implement your code here.

    for updated in surrounding_cells:
        new_x = x + updated[0]
        new_y = y + updated[1]
        #check boundaries
        if new_x >= len(input_board) or new_x < 0:
            continue

        if new_y >= len(input_board[new_x]) or new_y < 0:
            continue

        if input_board[new_x][new_y] == old:
            input_board[new_x] = input_board[new_x][:new_y] + new + input_board[new_x][new_y+1:]
            flood_fill(input_board, old, new, new_x, new_y)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....