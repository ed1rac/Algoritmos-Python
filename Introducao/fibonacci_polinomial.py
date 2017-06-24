def fib2(n):
    if n==0:
        return 0
    else:
        vetor=list(range(n+1))
        vetor[0]=0
        vetor[1]=1
        for i in range(2,n+1):
            vetor[i]=vetor[i-1]+vetor[i-2]

        return vetor[n]

#print fib2(12)
for i in range(0,50+1):
    print 'fib2(' + str(i) + ')=' + str(fib2(i))