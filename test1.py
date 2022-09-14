s=str(input())

if any(( ',' in s ) for a in s ):
    print('Found')
else:
    print('Not Found')
