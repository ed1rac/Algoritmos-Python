from array import array

vetor_inteiros = array('b', [1, 2, 3])
print(vetor_inteiros)

vetor_inteiros.insert(3, 4)
print(vetor_inteiros)

print(vetor_inteiros.index(2))  # posição do elemento 2 (começa em 0)

vetor_inteiros.insert(2, 10)
print(vetor_inteiros)
