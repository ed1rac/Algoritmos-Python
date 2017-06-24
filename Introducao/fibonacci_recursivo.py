# coding=utf-8
def fib1(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib1(num-1)+fib1(num-2)


for i in range(0,50+1):
    print 'fib1(' + str(i) + ')=' + str(fib1(i))


#print fib1(23)