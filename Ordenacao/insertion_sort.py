def ordenacao_por_insercao(arr):
    """
    Procedimento ordenacao_por_insercao
    extraido diretamente do livro Algoritmos de Thomas Cormen (pag 31) - o livro pequeno
    :param arr: uma lista de elementos
    :return: a lista ordenada
    """
    i = 1
    for i in range(len(arr)):
        chave = arr[i]
        j = i-1
        while j>=0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = chave
        print(arr)
    return arr


print (ordenacao_por_insercao([5, 3, 6, 2, 10, 12, 1, 20]))
print (ordenacao_por_insercao(['Led Zeppelin', 'Beatles', 'Rolling Stones', 'ABBA', 'Metallica', 'Deep Purple']))
