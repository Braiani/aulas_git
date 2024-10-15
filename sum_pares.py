#
# - Receber 10 números e somar os pares
#

lista = []
soma = 0
for i in range(10):
    digitado = int(input(f"Digite o {i+1}º número inteiro na lista: "))
    lista.append(digitado)
    if digitado % 2 == 0:
        soma += digitado

print(f"Os números digitados foram: {lista}")
print(f"A soma dos números digitados foi: {soma}")