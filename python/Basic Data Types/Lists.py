arr = []
for i in range(int(raw_input())):
    s = raw_input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print arr.index(s[1])
    elif s[0] == "count":
        print arr.count(s[1])
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print arr
