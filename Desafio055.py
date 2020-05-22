print(f"\033[;1m{'Desafio 055 - O maior e o menor numero':*^70}\033[m")
quant = int(input("Quantidade de números: "))
menor = 99999
maior = 0
aux_maior = -1
aux_menor = -1

for c in range(0,quant):
    print(f"Usuário {c+1}, ",end='')
    peso = float(input("Peso: "))
    if peso >= maior:
        maior = peso
        aux_maior = c
    if peso <= menor:
        menor = peso
        aux_menor = c


print(f"O mais pesado é o usuário {aux_maior+1} com {maior} kilos")
print(f"O mais leve é o usuário {aux_menor+1} com {menor} kilos")
