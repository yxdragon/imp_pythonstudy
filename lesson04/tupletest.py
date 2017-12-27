# name, math, chinese, english
lst = [('a', 3, 6, 10),
       ('c', 5, 9, 8),
       ('b', 8, 9, 0)]

nlst = sorted([(sum(i[1:]), i) for i in lst], reverse=True)
print(nlst)
lst = [i[1] for i in nlst]
print(lst)
