def fib(lim, rst=[], level=1, a=1, b=0):
    if lim==1:del rst[:]
    rst.append(a+b)
    if level==lim:return rst
    return fib(lim, rst, level+1, b, a+b)

if __name__ == '__main__':
    lst = fib(5)
