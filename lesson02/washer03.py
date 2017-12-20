print('请输入水位：')
level = input()

# 这是洗衣流程
if level=='low':
    print('注水 20L')
    print('搅拌 30m')
if level=='high':
    print('注水 50L')
    print('搅拌 60m')
print('放水')

# 这是甩干流程
print('请输入甩干次数：')
times = int(input())
for i in range(times):
    print('注入清水 30L')
    print('搅拌 20m')
    print('放水')
    print('甩干')

