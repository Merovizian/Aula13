print(f"\033[;1m{'Desafio 050 - Soma entre numeros pares':*^70}\033[m")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
soma = 0
for c in range(inicio, fim+1):
    numero = int(input(f"Digite o {c-(inicio-1)} número: "))
    if numero % 2 == 0:
        soma += numero
print(f"A somatoria dos numeros é {soma}")
