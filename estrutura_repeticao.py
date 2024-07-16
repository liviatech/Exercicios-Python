
# numero = int(input("Digite seu numero: "))
# if numero > 0 :
#     print('Numero positivo')
# else: 
#     print('Numero é negativo')


# numero = -1
# while numero < 0 :
#     numero = int(input("Digite seu numero: "))
# print ("Numero positvo inserido com sucesso!")

# frutas = ['maçã', 'banana', 'uva']#declarando uma lista
# for fruta in frutas :#for lemos para cada
#     print (fruta)

# numero1 = int(input("Digite um numero: "))
# numero2 = int(input("Digite um numero: "))
# if numero1 > numero2 :
#      print(str(numero1) + ' é o maior')
# else: 
#        print(str(numero2) + ' é o maior')

  
#  2.Faça um Programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.Imprima a mensagem "BomDia!" BoaTarde!"ou"BoaNoite!"ou"ValorInválido!",conforme o caso

# turno = input('O turno de estudo é  (M) Matutino ou (V) Vespertino ou (N) Noturno? ').strip().upper()
# if  turno == 'M' :
#     print('Bom Dia!')
# if turno == 'V':
#     print('Boa tarde!')
# if turno == 'N':
#     print('Boa Noite!')
# else:
#     print('Turno inválido!')


# 3.Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# nota = int(input('Digite uma nota de 0 a 10 : '))
# if nota < 0 or nota > 10 :
#     print('Valor inválido')
# else :
#     print('Parabéns')


# 4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame.O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado

# nota = int(input('Digite uma nota de 0 a 10 : '))
# if nota >= 7 :
#      print('Aluno Aprovado')
# else :
#      print('Aluno Reprovado')


# 5.Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique -o como equilátero, isósceles ou escaleno.
# equilátero:todos os lados com o mesmo valor
# isósceles:dois lados com o mesmo valor
# escaleno:todos os lados com medidas distintas.

# lado = float(input('Digite o valor do lado do triângulo: '))
# lado2 = float(input('Digite o valor do lado do triângulo: '))
# lado3 = float(input('Digite o valor do lado do triângulo: '))
# if lado == lado2 ==lado3 :
#     print('Triângulo equilátero')
# if lado == lado2 or lado == lado3 or lado2==lado3:
#     print('Triângulo Isósceles')
# else:
#     print('Triângulo Escaleno')


# 6.Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123",caso contrário imprima uma mensagem de erro

# usuario =str(input('Digite usuario : '))
# senha = str(input('Digite senha : '))
# if usuario!= "admin" and senha !=  "admin123" :
#     print('Acesso Negado')
# else:
#     print('Acesso Liberado')
 
 
 
# 7. Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente,adulto ou idoso. 

# idade = int(input('Digite idade: '))

# if idade <= 10:
#     print('É uma criança')
# elif idade <=18:
#         print('É um adolescente')
# elif idade <=60 : 
#     print('É um adulto')
# else:
#     print('É um idoso')
    
    

# #  8.Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.
# numero1 = float(input('Digite um numero: '))
# numero2 = float(input('Digite um numero: '))
# numero3 = float(input('Digite um numero: '))

# if numero1 > numero2  and numero1 > numero3:
#     print ('O primeiro numero é maior  ' + str(numero1))
# elif numero2 > numero1 and numero2 > numero3:
#      print ('O segundo numero é maior  ' + str(numero2))
# else :
#      print ('O terceiro numero é maior  ' + str(numero3) )
    

# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos.O processo de leitura deve ser encerrado quando o usuário informar o valor zero.Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos. 
 

# numero = int(input('Digite um número positivo (ou 0 para encerrar): '))
# if numero == 0:
#     print(' Leitura Encerrada ')
# elif numero < 0:
#     print("Por favor, digite um número positivo.")
# elif numero % 2 == 0:
#      print('Esse numero é par ',  + numero)
# else:
#      print('Esse numero é impar ', + numero)
  
 
 
 
# 10. Faça um programa que lê três números inteiros e os mostra em ordem crescente. 

# numero1 = int(input('Digite um numero inteiro: '))
# numero2 = int(input('Digite um numero inteiro: '))
# numero3 = int(input('Digite um numero inteiro: '))


# # Coloca os números em uma lista
# numeros = [numero1, numero2, numero3]

# # Ordena a lista em ordem crescente
# numeros_ordenados = sorted(numeros)

# # Mostra os números em ordem crescente
# print('Os números em ordem crescente são:', numeros_ordenados)



 
 
 
#  11.Escreva um programa que calcule o salário líquido.Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda. 
#  ●Renda até R$1.903,98:isentodeimpostoderenda;
#  ●Renda entre R$1.903,99 e R$2.826,65:alíquotade7,5%;
#  ●Renda entre R$2.826,66eR$3.751,05:alíquotade15%;
#  ●Renda entre R$3.751,06eR$4.664,68:alíquotade22,5%;
#  ●Renda acima de R$4.664,68:alíquotamáximade27,5%   
    
 # Solicita ao usuário o valor da renda
# renda = float(input('Digite o valor da renda: '))

# # Verifica a faixa de renda e calcula o imposto
# if renda <= 1903.98:
#     print('Salário isento de Imposto de Renda')
# elif 1903.99 <= renda <= 2826.65:
#     porcentagem = 7.5
#     imposto = (renda * porcentagem) / 100
#     salario_liquido = renda - imposto
#     print(f'Salário líquido é: {salario_liquido:.2f}')
# elif 2826.66 <= renda <= 3751.05:
#     porcentagem = 15
#     imposto = (renda * porcentagem) / 100
#     salario_liquido = renda - imposto
#     print(f'Salário líquido é: {salario_liquido:.2f}')
# elif 3751.06 <= renda <= 4664.68:
#     porcentagem = 22.5
#     imposto = (renda * porcentagem) / 100
#     salario_liquido = renda - imposto
#     print(f'Salário líquido é: {salario_liquido:.2f}')
# elif renda > 4664.68:
#     porcentagem = 27.5
#     imposto = (renda * porcentagem) / 100
#     salario_liquido = renda - imposto
#     print(f'Salário líquido é: {salario_liquido:.2f}')
# else:
#     print('Digite um valor válido')
