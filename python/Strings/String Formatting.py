def print_formatted(number):
    # your code goes here
    n = number
    width = len("{0:b}".format(n))
    for i in xrange(1,n+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)