def fat(x):
    if x==1:
        return 1
    else:
        return x * fat(x-1)


for i in range(1,20+1):
    print '%d! = %g' % (i, fat(i))