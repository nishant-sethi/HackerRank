import math


def std(subject_marks, avg, n):
    ans = 0
    for i in subject_marks:
        ans += (avg - i) ** 2

    return math.sqrt(ans / (n - 1))


def cof(u, v, avg_u, avg_v, std_u, std_v, n):
    ans = 0
    for i in range(n):
        ans += u[i] * v[i]

    ans -= (n * avg_u * avg_v)
    return ans / ((n - 1) * std_u * std_v)


n = int(input())
m = []
p = []
c = []
sum_m = 0
sum_c = 0
sum_p = 0

for _ in range(n):
    m_, p_, c_ = map(int, input().split('\t'))
    m.append(m_)
    p.append(p_)
    c.append(c_)

avg_m = sum(m) / n
avg_c = sum(c) / n
avg_p = sum(p) / n

std_m = std(m, avg_m, n)
std_p = std(p, avg_p, n)
std_c = std(c, avg_c, n)

print(round(cof(m, p, avg_m, avg_p, std_m, std_p, n), 2))
print(round(cof(c, p, avg_c, avg_p, std_c, std_p, n), 2))
print(round(cof(m, c, avg_m, avg_c, std_m, std_c, n), 2))