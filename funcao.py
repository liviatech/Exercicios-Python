# def soma(num1, num2): #definição da função soma
#     calculo = num1 + num2
#     print(f'O resultado da soma é: {calculo}')


# def subtracao(num1, num2):    
#     sub = num1 - num2
#     print(f'O resultado da subtração e {sub}')
    
# def multiplicacao(num1, num2): # recebe as variáveis
#     multi = num1 * num2
#     print(f'O resultado da multiplicação é {multi}')
    
# def divisao(num1, num2):
#     div = num1 / num2
    
#     print(f'O resultado da divisão é {div}')
    
# num1 = int(input('Digite o primeiro número: ')) # parâmetros
# num2 = int(input('Digite o segundo número: '))
# soma(num1, num2) # chamada da função   
# subtracao(num1, num2)
# multiplicacao(num1, num2)
# divisao(num1, num2)


#Manipulação de arquivos
# def multiplicacao(num1, num2):  # recebe as variáveis
#     multi = num1 * num2
#     file = 'arquivo.txt'
    
#     # abertura para escrita
#     arquivo_escrita = open(file, "w")
#     arquivo_escrita.write(f'O resultado da multiplicação é {multi}')
#     arquivo_escrita.close()
    
#     # leitura
#     arquivo_leitura = open(file, "r")
#     leitura = arquivo_leitura.read()
#     print(leitura)
#     arquivo_leitura.close()
      
# # Chamada da função com os argumentos num1 e num2
# multiplicacao(3, 4)

#TRATAMENTO DE EXCEÇÕES
def divisao(a,b):
    try:
    resultado = a/b
    print(resultado)
    
    exception ZeroDivisionError:
    print("Erro: Impossível divisão por zero")
    Exception TypeError as e:
    print(f'Erro: O tipo do dado informado está incorreto. /n')
    else:
        print('Sem exceções')

    
divisao()