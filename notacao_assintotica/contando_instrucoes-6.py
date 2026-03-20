# -*- encoding: utf-8 -*-
"""
exemplo 6 - for
============================================
inicialização do i -> 1 instrução
comparacoes com o n -> 1 + n instrucoes
incremento do i --> n instruções
impressao --> n instruções
>>>>---- 3n + 3 instrucoes no total ----<<<<
============================================
"""
n = 10                    # --> 1
for i in range(0,n+1):    # --> 1 + 1 + n + n
    print(i)              # --> n 

