# coding=utf-8
def max(lista):
  if len(lista) == 2:
    return lista[0] if lista[0] > lista[1] else lista[1]
  sub_max = max(lista[1:])
  return lista[0] if lista[0] > sub_max else sub_max


lista=[12,45,67,11,10,34]
print 'A lista é: ' + str(lista)
print 'O maior elemento é: %d' % (max(lista))