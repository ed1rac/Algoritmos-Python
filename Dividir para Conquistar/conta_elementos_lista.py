def count(lista):
  if lista == []:
    return 0
  return 1 + count(lista[1:])


lista=[1,2,3,4,5,6,7,8,9,10]
print 'Existem ' + str(count(lista)) + ' elementos na lista'