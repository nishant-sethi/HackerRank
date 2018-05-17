m=raw_input()
m_list=set(map(int,raw_input().split()))
n=raw_input()
n_list=set(map(int,raw_input().split()))
x=m_list.difference(n_list)
y=n_list.difference(m_list)
z=x.union(y)
a=list(z)
a.sort()
for i in a:
    print i