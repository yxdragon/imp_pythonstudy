def fib3(a, b):
    print(a+b)

def fib2(a, b):
    print(a+b)
    fib3(b, a+b)

def fib1(a, b):
    print(a+b)
    fib2(b, a+b)

#fib1(1,1)

def fib(lim, level=1, a=1, b=0):
    print(a+b)
    if level==lim:return
    fib(lim, level+1, b, a+b)

fib(10)
