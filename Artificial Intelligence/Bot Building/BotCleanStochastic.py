#!/bin/python
# Head ends here
class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

def nextMove(posx, posy, board):
    # the input x and y were reversed in Hackerrank puzzles.
    bot_node = Node(posy, posx)

    # find the nearest dirty node.
    nearest_node = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":
                dirty_node = Node(j, i)
                dist = dirty_node.distTo(bot_node) 
                
                #bot at the dirty node.
                if dist == 0:
                    print "CLEAN"
                    return

                if nearest_node is None or dist < nearest_node.distTo(bot_node):
                    nearest_node = dirty_node

    # path finding.
    output = None
    if nearest_node is not None:
        delta_x = nearest_node.x - bot_node.x
        if delta_x < 0:
            output = "LEFT"
        elif delta_x > 0:
            output = "RIGHT"

        if output is not None:
            print output
            return

        delta_y = nearest_node.y - bot_node.y
        if delta_y < 0:
            output = "UP"
        elif delta_y > 0:
            output = "DOWN"

        if output is not None:
            print output
            return

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)