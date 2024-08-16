#Com base nos conhecimentos adquiridos ao longo desta aula, faça um programa em Python que use lista ou função.

# Fiz uma função para remover duplicatas de uma lista:
def remover_duplicatas(lista):
    lista_unica = list(set(lista))  
    return lista_unica


lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]


lista_sem_duplicatas = remover_duplicatas(lista_com_duplicatas)


print("Lista original com duplicatas:", lista_com_duplicatas)
print("Lista após remover duplicatas:", lista_sem_duplicatas)
