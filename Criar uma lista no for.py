lista =''
for a in range(0,5):
    numero = (input("digite: "))

    lista = lista + numero
    if a < 4:
        lista = lista + ','

print(lista.split(','))
