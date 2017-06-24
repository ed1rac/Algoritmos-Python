def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])


lista = [1,2,3,4, 5]
#print lista[1:] #slice
#print lista[1:3] #slice
print sum(lista)