print(f"\033[;1m{'Desafio 050 - Soma entre numeros pares':*^70}\033[m")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
soma = 0
for c in range(inicio, fim):
    if c % 2 == 0:
        soma += c
print(soma)
