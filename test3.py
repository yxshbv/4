s = str(input())
list1 = []
list1 = list(s.strip(' '))
x = 0
for i in s:
    if i.isdigit():
        x+=1
print(x)
