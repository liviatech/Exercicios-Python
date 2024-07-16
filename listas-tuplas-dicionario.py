# #listas

# lista_frutas = []#declaração da lista
# lista_frutas.append('Maçã')
# lista_frutas.append('Uva')
# lista_frutas.append('Banana')
# nova_fruta = input('Digite o nome de uma fruta: ')  # solicita entrada do usuário
# lista_frutas.append(nova_fruta)  # adiciona a nova fruta à lista
# print(lista_frutas)

# tupla = ('maçã','pera', 'abacaxi', 'limão')
# print(tupla)

# dicionario = {'chave': 'valor'}
# dicionario['maça'] = 'É uma fruta'
# dicionario['carro'] = 'É um veículo'
# dicionario['gato'] = 'E um animal'
# print(dicionario)


# 1.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: Telefonou para a vítima?Esteve no local do crime? Mora perto da vítima? Devia para a vítima? Já trabalhou com a vítima?O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como  Suspeita, entre 3 e 4 como Cúmplice  e 5 como Assassino. Caso contrário, ele será classificado como Inocente.

# lista_respostas = []  # Use plural para indicar que a lista armazena múltiplas respostas

# # Coleta as respostas do usuário e armazena na lista
# lista_respostas.append(input('Telefonou para a vítima? '))
# lista_respostas.append(input('Esteve no local do crime? '))
# lista_respostas.append(input('Mora perto da vítima? '))
# lista_respostas.append(input('Devia para a vítima? '))
# lista_respostas.append(input('Já trabalhou com a vítima? '))

# # Conta quantas respostas são 'sim'
# num_sim = lista_respostas.count('sim')

# # Determina a classificação com base no número de respostas 'sim'
# if num_sim == 2:
#     print('Suspeito')
# elif num_sim == 3 or num_sim == 4:
#     print('Cúmplice')
# elif num_sim == 5:
#     print('Assassino')
# else:
#     print('Inocente')



#  2.Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno,
#  imprima o número de alunos com média maior ou igual a 7.0. 
# Função para calcular a média das notas de um aluno
# def calcular_media(notas):
#     soma = sum(notas)
#     quantidade = len(notas)
#     media = soma / quantidade
#     return media

# # Coletar as notas dos alunos
# lista_notas_aluno1 = [float(input('Nota 1 aluno 1: ')), float(input('Nota 2 aluno 1: ')), float(input('Nota 3 aluno 1: ')), float(input('Nota 4 aluno 1: '))]
# lista_notas_aluno2 = [float(input('Nota 1 aluno 2: ')), float(input('Nota 2 aluno 2: ')), float(input('Nota 3 aluno 2: ')), float(input('Nota 4 aluno 2: '))]
# lista_notas_aluno3 = [float(input('Nota 1 aluno 3: ')), float(input('Nota 2 aluno 3: ')), float(input('Nota 3 aluno 3: ')), float(input('Nota 4 aluno 3: '))]
# lista_notas_aluno4 = [float(input('Nota 1 aluno 4: ')), float(input('Nota 2 aluno 4: ')), float(input('Nota 3 aluno 4: ')), float(input('Nota 4 aluno 4: '))]
# lista_notas_aluno5 = [float(input('Nota 1 aluno 5: ')), float(input('Nota 2 aluno 5: ')), float(input('Nota 3 aluno 5: ')), float(input('Nota 4 aluno 5: '))]

# # Calcular as médias dos alunos
# media_aluno1 = calcular_media(lista_notas_aluno1)
# media_aluno2 = calcular_media(lista_notas_aluno2)
# media_aluno3 = calcular_media(lista_notas_aluno3)
# media_aluno4 = calcular_media(lista_notas_aluno4)
# media_aluno5 = calcular_media(lista_notas_aluno5)

# # Listar as médias
# medias = [media_aluno1, media_aluno2, media_aluno3, media_aluno4, media_aluno5]

# # Contar quantos alunos atingiram a média de 7 ou mais
# num_alunos_com_media = sum(1 for media in medias if media >= 7)

# print(f'Número de alunos que atingiram a média: {num_alunos_com_media}')






# 3.Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho.Calcule o total do carrinho de compra. 

# compras = {} 
# compras ['bala'] = 5.00
# compras ['carne'] = 30.00
# compras [ 'feijão'] = 25.00
# compras['alho'] = 10.00

# total = sum(compras.values())

# print(f'O total é :   {total}')




# 4.Crie um dicionário representando contatos (nome,telefone). Permita ao usuário procurar por um contato pelo nome. 


# contatos = {}
# contatos['Maria'] = '1111-1111'
# contatos['João'] =' 2222-2222'
# contatos['Carmem']='3333-3333'
# contatos['Paulo']= '4444-4444'
# contatos['Darcy']= '5555-5555'

# busca = input('Digite o nome : ')

# if busca in contatos:
#     print(f'O número de {busca} é: {contatos[busca]}')
# else:
#     print('Nome não encontrado.')


# 5.Crie duas tuplas. Concatene-as para formar uma nova tupla. 
# frutas = ('maçã','uva', 'banana')
# animais = ('cobra', 'cavalo', 'boi')
# total = frutas  + animais
# print (total)




# 6.Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# nome = input('Digite seu nome: ')

# nome_maiusculo = nome.upper()


# nome_revertido = nome_maiusculo[::-1]

# print(f'O nome revertido é: {nome_revertido}')
