num = int(input("Digite o número que deseja calcular o fatorial (!): "))

resultado = num
for i in range((num - 1), 0, -1):
    resultado *= i

print(f"Resultado do fatorial: {resultado}")