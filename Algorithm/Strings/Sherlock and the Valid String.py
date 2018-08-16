import collections
s = input().strip()
freq = collections.Counter(s)
values = list(freq.values())
values.sort()
print('YES' if values.count(values[0]) == len(values) or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) or (values.count(values[-1]) == len(values) - 1 and values[0] == 1) else 'NO')
        