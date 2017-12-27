lst = [1,3,5,7,5,3,5]

def one(lst):
    nlst = []
    for i in lst:
        has = False
        for j in nlst:
            if i==j:has=True
        if not has:
            nlst.append(i)
    return nlst

def one_in(lst):
    nlst = []
    for i in lst:
        if not i in nlst:
            nlst.append(i)
    return nlst

print(one(lst))
print(one_in(lst))
print(list(set(lst)))

