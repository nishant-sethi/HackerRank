#!/usr/bin/env python

def displayPathToPrincess(n, grid):
    # find princess and mario
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    
    # negative row difference implies UP
    # negative col difference implies LEFT
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]

    return ''.join([
        'UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows,
        'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols])


# org-babel variable check
if '_input' in globals():
    _input = _input.strip().split()
    m = int(_input[0], 10)
    grid = _input[1:]
else:
    m = input()
    grid = []

    for i in xrange(0, m):
        grid.append(raw_input().strip())

print displayPathToPrincess(m, grid)