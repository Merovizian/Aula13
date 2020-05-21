for cont in range(0, 11, 5):
   print (cont)

n = int(input("Digite um valor máximo: "))
for c in range(0, n+1):
    print(c)
print("Fim")


ranger = (input("Informe um intervalo (min/max): "))
ranger_min = int(ranger[0:(ranger.find('/'))])
ranger_max = int(ranger[(ranger.find('/')) + 1:])
if ranger_min > ranger_max:
    print("\033[1;31mERROR!! - Informe um intervalo válido!")

for c in range(ranger_min, ranger_max):
    print(f"{c}",end=',')
print(c+1)