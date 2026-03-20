f_an = [(n ** 2 - n + 549) for n in range(200)]
f_bn = [(49 * n + 49) for n in range(200)]

print(f_an)

for i in range (200):
    if f_an[i]<=f_bn[i]:
        print('n = ', i, ' => a(n) = ', f_an[i], ' <=  b(n) = ', f_bn[i] )
        