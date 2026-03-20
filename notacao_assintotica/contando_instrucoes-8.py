# -*- encoding: utf-8 -*-
"""
exemplo 8 - for dentro de outro for
============================================
inicialização do i -> 1 instrução
comparacoes com o n -> 1 + n instrucoes
incremento do i --> n instruções
impressao --> n instruções
>>-- 3nˆ2 + 3n + 3 instrucoes no total --<<
============================================
"""       
n = 5                      # --> 1
for i in range(0,n):      # --> 2 + n * (
    for j in range(0,n):  #       2 + n + n
        print(i)            # --> n )  + n

"""
1 + 2 + n * ( 2 + n + n + n) + n = 
3 + n * (2 + 3n) + n
3 + 2n + 3nˆ2 + n = 
3nˆ2 + 3n + 3
"""

