import time
print(f"\033[;1m{'Desafio 46 - Programa de contagem regressiva':*^70}\033[;m")
tempo = int(input("Informe quantos segundos: "))
for c in range(tempo, 0, -1):
    print(c)
    time.sleep(1)
print("\033[1;31mTime is Over!")

