if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr=list(set(arr))
    arr.sort()
    print arr[len(arr)-2]