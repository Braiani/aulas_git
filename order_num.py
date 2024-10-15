#
# - Criar função para ordenar uma lista de números de forma crescente
#

lista = []
while True:
    try:
        lista.append(int(input("Digite um número para adicionar na lista (ctrl + c para ordenar): ")))
    except KeyboardInterrupt:
        break

print(f"Lista digitada por você: {lista}")

swapped = True
while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        temp = None
        if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                swapped = True

print(f"Lista ordenada: {lista}")