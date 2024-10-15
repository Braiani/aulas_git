#
# - Criar função para verificar se a palavra ou frase é palindromo
#

palavra = input("Digite a palavra que deseja verificar se é ou não Palindromo: ")

if palavra == ''.join(reversed(palavra)):
    print("A palavra digitada É palindromo!")
else:
    print("A palavra digitada NÃO É palindromo!")