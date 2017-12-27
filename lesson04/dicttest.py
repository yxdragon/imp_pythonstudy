txt = 'to be or not to be z z z'
def statistic(txt):
    dic = {}
    for i in txt.split(' '):
        if not i in dic:
            dic[i] = 1
        else: dic[i] += 1
    return dic
    
def sortword(dic):
    items = dic.items()
    nitems = [(i[1], i) for i in items]
    nitems.sort(reverse=True)
    items = [i[1] for i in nitems]
    print(items)

dic = statistic(txt)
sortword(dic)
