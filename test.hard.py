s = str ( input ()) 
main = list(s.split('.'))
l1 = main[0].split(' ')
l2 = main[1].split(' ')
counter = 0
for i in l1:
    for a in l2:
        if i == a:
            counter += 1
print (counter)
