print(f"\033[;1m{'Desafio 053 - Palindromo':*^70}\033[m")
frase = input("Digite a frase: ")
frase = frase.split()
frase = ''.join(frase)
tamanho = len(frase)
frase_inversa = ''
for c in range(tamanho-1, -1 ,-1):
  frase_inversa = frase_inversa + frase[c]
if frase == frase_inversa:
    print('É um palindromo!!')
else:
    print("Não é um palindromo!!")


## Método 2:

if frase == frase[::-1]:
    print("É um palindromo!")
else:
    print("Não é um palindromo!")
