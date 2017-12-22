def fac(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

print(fac(3))

def A(n, m):
    s = 1
    for i in range(n-m+1, n+1):
        s *= i
    return s

def A2(n, m):
    return fac(n)//fac(n-m)

print(A(4,3))
print(A2(4,3))

def C(n, m):
    return A2(n,m)//fac(m)

print(C(5,3))
print(C(5,2))
