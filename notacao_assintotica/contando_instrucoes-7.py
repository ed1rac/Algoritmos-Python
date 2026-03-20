# -*- encoding: utf-8 -*-
"""
exemplo 6 - for
============================================
inicialização do i -> 1 instrução
comparacoes com o n -> 1 + (n - 1) instrucoes
incremento do i --> n - 1 instruções
impressao --> n - 1 instruções
>>>>---- 4n - 1 instrucoes no total ----<<<<
============================================
"""
a = 0                       # --> 1
n = 10                      # --> 1
for i in range(1,n+1):      # --> 1 + 1 + (n - 1) + (n - 1)
    a = a+1                 # --> (n - 1)
    print(i)                # --> (n - 1) 
print('a = ', a)            # --> 1