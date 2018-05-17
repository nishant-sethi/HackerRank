#!/bin/python
# Head ends here
def nextMove(n, x, y, grid):
    # the input x and y were reversed in Hackerrank puzzles.
    start_x, start_y = y, x
    
    # find the princess node.
    end_x, end_y = 0, 0
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == "p":
                end_x = j
                end_y = i

    # path finding.
    delta_x = end_x - start_x
    if delta_x > 0:
        print "RIGHT";
        return
    elif delta_x < 0:
        print "LEFT"
        return

    delta_y = end_y - start_y
    if delta_y > 0:
        print "DOWN"
        return
    elif delta_y < 0:
        print "UP"
        return

# Tail starts here
n = input()
x,y = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

nextMove(n, x, y, grid)