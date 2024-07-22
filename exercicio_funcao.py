#Exercícios Funções e Extras de Python 

#1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''
# Solicitação dos parâmetros ao usuário
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# num3 = int(input('Digite o terceiro número: '))


# def soma(num1, num2, num3):  # Definição da função soma
#     calculo = num1 + num2 + num3
#     print(f'O resultado da soma é: {calculo}')


# # Chamada da função com os parâmetros fornecidos pelo usuário
# soma(num1, num2, num3)



#'''2.Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo:127->721.'''
# def troca(numero):     # Converte o número para uma string
#     numero_str = str(numero)
    
   
#     numero_revertido_str = numero_str[::-1]  # Reverte a string
    
   
#     numero_revertido = int(numero_revertido_str)  # Converte a string revertida de volta para um número
    
#     return numero_revertido

# # Solicita um número ao usuário
# numero = int(input('Digite um número com mais de 3 dígitos: '))

# # Chama a função e imprime o resultado
# resultado = troca(numero)
# print(f'O número revertido é: {resultado}')


#'''3.Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta. '''
# def converter_fahrenheit(celsius):
#     """Converte a temperatura de Celsius para Fahrenheit e imprime o resultado."""
#     fahrenheit = (celsius * 9/5) + 32
#     print(f'O valor em Fahrenheit é: {fahrenheit:.2f}')

# def converter_celsius(fahrenheit):
#     """Converte a temperatura de Fahrenheit para Celsius e imprime o resultado."""
#     celsius = (fahrenheit - 32) * 5/9
#     print(f'O valor em Celsius é: {celsius:.2f}')

# def escolha(resposta, valor):
#     """Escolhe qual conversão fazer com base na resposta do usuário e imprime o resultado."""
#     if resposta.lower() == 'celsius':
#         converter_celsius(valor)
#     elif resposta.lower() == 'fahrenheit':
#         converter_fahrenheit(valor)
#     else:
#         print("Resposta inválida. Por favor, digite 'Celsius' ou 'Fahrenheit'.")

# # Solicita a escolha do usuário
# resposta = input('Digite "Celsius" para converter a temperatura em Celsius ou "Fahrenheit" para converter a temperatura em Fahrenheit: ')

# # Solicita o valor da temperatura
# valor = float(input('Digite o valor da temperatura: '))

# # Faz a conversão e imprime o resultado
# escolha(resposta, valor)



#'''4.Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar  de cada moeda estrangeira. Considere a tabela de conversão abaixo: DólarAmericano:R$ 4,91 Peso Argentino:R$ 0,02 
#Dólar Australiano:R$3,18  DólarCanadense:R$3,64  FrancoSuiço:R$0,42  Euro:R$5,36  Libraesterlina:R$6,21 '''
# def converter_moeda(valor_carteira, taxa_cambio):
#     """Converte o valor da carteira para uma moeda estrangeira com base na taxa de câmbio."""
#     return valor_carteira / taxa_cambio

# def main():
#     # Taxas de câmbio
#     taxas_cambio = {
#         'Dólar Americano': 4.91,
#         'Peso Argentino': 0.02,
#         'Dólar Australiano': 3.18,
#         'Dólar Canadense': 3.64,
#         'Franco Suíço': 0.42,
#         'Euro': 5.36,
#         'Libra Esterlina': 6.21
#     }

#     # Solicita o valor da carteira ao usuário
#     valor_carteira = float(input('Digite o valor da sua carteira em reais: '))

#     # Calcula e imprime o valor que pode ser comprado em cada moeda
#     print("\nVocê pode comprar o seguinte com R$ {:.2f}:".format(valor_carteira))
#     for moeda, taxa in taxas_cambio.items():
#         valor_moeda = converter_moeda(valor_carteira, taxa)
#         print(f'{moeda}: {valor_moeda:.2f}')

# if __name__ == "__main__":
#     main()







#'''5.Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário  para inserir uma  frase e utilize a função para contar as vogais.'''

# def contar_vogais(frase):
#     """Conta o número de vogais em uma frase e imprime o resultado."""
#     vogais = ['a', 'e', 'i', 'o', 'u']
#     contador = 0
    
#     frase = frase.lower()  # Converter para minúsculas
    
#     for letra in frase:  # Contar as vogais
#         if letra in vogais:
#             contador += 1
    
#     print(f'A quantidade de vogais é: {contador}')

# # Solicitar a frase ao usuário
# frase = input('Digite uma frase: ')

# # Chamar a função com a frase fornecida
# contar_vogais(frase)


#'''6.Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra
 #da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o  jogador pode  fornecer uma letra. Se a letra estiver presente na palavra secreta, ela  será revelada nas posições correspondentes.Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. Dica: Você precisará importar uma biblioteca para resolver esse exercício'''
 
# import random

# def escolher_palavra():
#     """Escolhe uma palavra aleatória de uma lista predefinida."""
#     palavras = ['python', 'programacao', 'desenvolvedor', 'algoritmo', 'computador']
#     return random.choice(palavras)

# def exibir_palavra(palavra_secreta, letras_adivinhadas):
#     """Retorna a palavra secreta com as letras adivinhadas reveladas."""
#     return ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])

# def jogo_forca():
#     """Executa o jogo de Forca."""
#     palavra_secreta = escolher_palavra()
#     letras_adivinhadas = set()
#     tentativas_restantes = 6
#     letras_erradas = set()

#     print("Bem-vindo ao jogo da Forca!")
#     print("Tente adivinhar a palavra.")

#     while tentativas_restantes > 0:
#         print("\n" + exibir_palavra(palavra_secreta, letras_adivinhadas))
#         print(f"Tentativas restantes: {tentativas_restantes}")
#         print(f"Letras erradas: {', '.join(letras_erradas)}")

#         tentativa = input("Digite uma letra: ").lower()

#         if tentativa in letras_adivinhadas or tentativa in letras_erradas:
#             print("Você já tentou essa letra.")
#         elif tentativa in palavra_secreta:
#             letras_adivinhadas.add(tentativa)
#             if set(palavra_secreta) <= letras_adivinhadas:
#                 print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
#                 break
#         else:
#             letras_erradas.add(tentativa)
#             tentativas_restantes -= 1
#             print("Letra incorreta.")

#         if tentativas_restantes == 0:
#             print(f"Você perdeu! A palavra era: {palavra_secreta}")

# # Executar o jogo
# jogo_forca()
