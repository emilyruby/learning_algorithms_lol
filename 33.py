# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. The move sequence is represented by a string. And each move
# is represent by a character. The valid robot moves are R (Right), L (Left),
# U (Up) and D (down). The output should be true or false representing whether
# the robot makes a circle.


def robot(position, moves):

    x, y = position
    seq = list(moves)

    move = {
        'R': [0, 1],
        'L': [0, -1],
        'U': [1, 0],
        'D': [-1, 0]
    }

    for m in seq:
        x, y = x + move[m][0], y + move[m][1]

    if x == position[0] and y == position[1]:
        return True

    return False
