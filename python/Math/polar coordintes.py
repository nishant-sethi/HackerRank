import cmath
num=input()
comp_num=complex(num)
result=cmath.phase(comp_num)
print((comp_num.real**2+comp_num.imag**2)**0.5)
print(result)