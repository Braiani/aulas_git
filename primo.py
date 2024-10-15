#
# - Criar função para verificar se um número é primo
#

numero = int(input("Digite um número inteiro e saiba se ele é primo: "))

if numero < 1:
    print("Para ser número primo, precisa ser maior que 1")
    exit()

primo = True

if numero > 2:
    for i in range(2, numero - 1):
        if numero % i == 0:
            primo = False



if primo:
    print("O número digitado É primo")
else:
    print("O número digitado NÃO É primo")