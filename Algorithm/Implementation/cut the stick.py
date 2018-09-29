N = input()
num = map(int, raw_input().split())
val = [0] * 1001
for i in num:
    val[i] += 1
counter = 0
val = val[::-1]
ans = []
for i in val:
    if i > 0:
        counter += i
        ans.append(counter)
ans = ans[::-1]
for i in ans:
    print i
