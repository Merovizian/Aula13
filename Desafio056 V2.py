limite_cadastro = int(input("Quantos cadastros: "))
database_masculino = ('m','M','masculino','Masculino','MASCULINO')
database_feminino = ('f', 'F', 'Feminino', 'FEMININO', 'feminino')
lista_homens = ''
lista_mulheres = ''
lista_20anos = ''
soma_idades = 0
aux_homem = 0

for c in range(0, limite_cadastro):
    nome = input("QUAL SEU NOME: ")
    sexo = input("Qual o sexo: ")
    idade = input("Qual a sua idade: ")
    soma_idades += int(idade)
    for d in range (0,5):
        if sexo == database_masculino[d]:
            lista_homens += nome
            lista_homens += '-'
            lista_homens += idade
            lista_homens += '.'
        if sexo == database_feminino[d]:
            lista_mulheres += nome
            lista_mulheres += '-'
            lista_mulheres += idade
            lista_mulheres += '.'

separa_homens = lista_homens[:len(lista_homens) - 1].split('.')
separa_mulheres = lista_mulheres[:len(lista_mulheres) - 1].split('.')

if lista_homens != '':
    for d in range(0, len(separa_homens)):
        maior = int(separa_homens[d].split('-')[1])
        if maior > aux_homem:
            aux_homem = maior
            aux_nome = separa_homens[d].split('-')[0]

if lista_mulheres != '':
    for a in range(0, len(separa_mulheres)):
        menor = int(separa_mulheres[a].split('-')[1])
        if menor < 20:
            lista_20anos += separa_mulheres[a].split('-')[0]
            lista_20anos += ','

if lista_homens != '':
    print(f"O Homem mais velho é {aux_nome} com {aux_homem} anos")
if lista_mulheres != '':
    print(f"Existem {len(lista_20anos.split(','))-1} mulheres com menos de 20 anos que são: {lista_20anos[:len(lista_20anos) - 1]}")
if limite_cadastro != 0:
    print(f"A somatoria das idades é: {soma_idades / limite_cadastro}")
