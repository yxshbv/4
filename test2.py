s = str ( input ())
a = []
a = list(s.strip(' '))
x = s.index('a')
y = s.rindex('o')
a.append('')
a[-1] = a[x]
a[x] = a[y]
a[y] = a[-1]
a.pop()
result=''
for i in a:
    result += i
print(result)
