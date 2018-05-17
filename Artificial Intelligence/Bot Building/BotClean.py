#!/bin/python
# Head ends here
class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

def next_move(posx, posy, board):
    # the input x and y were reversed in Hackerrank puzzles.
    bot_node = Node(posy, posx)

    dirty_nodes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":
                dirty_nodes.append(Node(j, i))

    # find the nearest dirty node.
    nearest_node = None
    for node in dirty_nodes:
        if nearest_node is None or node.distTo(bot_node) < nearest_node.distTo(bot_node):
            nearest_node = node

    if nearest_node is not None:
        print_move(nearest_node.x - bot_node.x, nearest_node.y - bot_node.y)

def print_move(delta_x, delta_y):
    if delta_x < 0 :
        print "LEFT"
    elif delta_x > 0 :
        print "RIGHT"
    elif delta_y < 0 :
        print "UP"
    elif delta_y > 0 :
        print "DOWN"
    else:
        print "CLEAN"

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)