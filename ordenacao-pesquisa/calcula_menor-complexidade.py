"""
Qual é a complexidade T(n) de calcula_menor?
A função faz n-1 comparações
Poderíamos dizer que a complexidade é T(n) = n-1?
No exemplo, temos n = 11
"""
def calcula_menor(vetor):
  menor = vetor[0]              # 1
  for i in range(len(vetor)):   # 1
    if vetor[i] < menor:        # 10  (n-1)
      menor = vetor[i]          # 1
                                # ------------
                                #  T(n) = (n-1) + 3
                                #  T(n) = n
    
  
  return menor


print(calcula_menor([10,9,8,7,6,5,4,3,2,1,0]))