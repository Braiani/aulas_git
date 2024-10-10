#
# - Criar função para exibir os n primeiros números da sequência fibbonacci
#
def fibonnacci(steps):
    sequencia = [0,1]
    if steps <= 2:
        return sequencia
    
    for i in range(2, steps):
        soma = sequencia[i-1] + sequencia[i-2]
        sequencia.append(soma)
    
    return sequencia
    
num = int(input("Digite quantos números da sequência de Fibonnacci deseja ver: "))

if num < 3:
    print("O mínimo de elementos são 2!")

sequencia = fibonnacci(num)

print(f"Sequência de Fibo: {sequencia}")