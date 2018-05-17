def capitalize(string):
    s=string
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s
