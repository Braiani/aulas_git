#
# - Criar tabuada com o número informado pelo usuário
#

tabuada = int(input("Digite qual a tabuada você deseja: "))
multiplicador = int(input("Você deseja o cálculo até qual valor: "))


if tabuada < 0 or multiplicador < 1:
    print("Valores inválidos!")
    exit()

for i in range(multiplicador + 1):
    print(f"{tabuada} x {i} = {tabuada * i}")