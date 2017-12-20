print('1+2+3...+100')
s = 0
for i in range(101):
    # s = s+i
    s += i
print(s)

print('1-100之间能够被100整除的数')
for i in range(1,101):
    if 100 % i == 0:print(i)

print('1-100之间，个位十位相加等于9的数字')
for i in range(1, 101):
    if i%2!=0:continue
    if i//10+i%10 == 9:
        print(i)

print('1-100之间，个位十位相加等于9的数字 5个')
s = 0
for i in range(1, 101):
    if i%2!=0:continue
    if i//10+i%10 == 9:
        print(i)
        s += 1
        if s==3:break
