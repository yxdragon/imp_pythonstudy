import os
os.mkdir('abc')

f = open('abc/abc.txt', 'w')
f.write('I love python!')
f.close()


f = open('abc/abc.txt')
print(f.readlines())
f.close()