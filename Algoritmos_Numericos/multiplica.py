# coding=utf-8
"""
Livro Algoritmos do Dasgupta
Autor: Ed - Data: 23/06/2017 - Observações: página 15 está o pseudocódigo e a discussão
"""
def multiplica(x,y):
    #entrada: dois inteiros de n bits x e y, onde y>=0
    #Saída: o produto deles
    if y==0:
        return 0
    if y%2==0:
        z = multiplica(x,int(y/2))
        return 2 * z
    else:
        z = multiplica(x, int(y / 2))
        return x + 2*z


print(multiplica(6,4))
