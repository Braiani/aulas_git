#
# - Criar função para converter temperatura de celsius para fahrenheit
# - Usuário deve escolher a conversão que deseja
#

def celsius_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32

def fahrenheit_celsius(temperatura):
    return (temperatura - 32) / 1.8


print("-= Seja bem-vindo ao programa de conversão de temperatura! =-")
print("-=        Iniciaremos a conversão da temperatuda           =-")

print("""
1 - Converter Celsius para Fahrenheit
2 - Converter Fahrenheit para Celsius
""")

opcao = input("Opção desejada: ")

temperatura = float(input("Digite a temperatura para conversão: "))

if opcao == "1":
    print(f"A temperatura convertida é {celsius_fahrenheit(temperatura=temperatura):.2f}ºF")
elif opcao == "2":
    print(f"A temperatura convertida é {fahrenheit_celsius(temperatura=temperatura):.2f}ºC")