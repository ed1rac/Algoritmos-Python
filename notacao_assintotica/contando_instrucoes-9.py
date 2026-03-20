# -*- encoding: utf-8 -*-
"""
exemplo 9 - if dentro de um for
============================================
inicialização do i -> 1 instrução
comparacoes com o n -> 1 + n instrucoes
incremento do i --> n instruções
impressao --> n instruções
>>-- 3nˆ2 + 3n + 3 instrucoes no total --<<
============================================
"""       
numeros = [1,2,3,4,5,6,7,8]         # --> 1
for i in range(0,len(numeros)):     # --> 2 + len(numeros)
    if numeros[i] %2== 0:           # 
    #print('numeros[', i , '] = ', numeros[i])            # --> n )  + n
        print(numeros[i])           # --> 4 (ou seja n/2)

"""
O if só vai executar (e contar) dependendo dos valores testados.
"""


