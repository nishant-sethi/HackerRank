if __name__ == '__main__':
    n = int(raw_input())
    if(n%2!=0):
        print "Weird"
    else:
        if(2 <= n <= 5):
            print "Not Weird"
        elif(6 <= n <= 20):
            print "Weird"
        else:
            print "Not Weird"