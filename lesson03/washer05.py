# 这是洗衣流程
def wash(level):
    if level=='low':
        print('注水 20L')
        print('搅拌 30m')
    if level=='high':
        print('注水 50L')
        print('搅拌 60m')
    print('放水')

# 这是甩干流程
def dry(times):
    for i in range(times):
        print('注入清水 30L')
        print('搅拌 20m')
        print('放水')
        print('甩干')

# **key
def wash_dry(obj, level='low', times=1):
    print('======== 开始洗衣 ========')
    wash(level)
    dry(times)
    print('%s 洗干净了'%obj)
    
wash_dry('衣服')
wash_dry('毛毯', 'high', 3)
wash_dry('xxx', times=2)
