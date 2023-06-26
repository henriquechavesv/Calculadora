print('Selecione a operação: ')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

opcoes_validas = [1, 2, 3, 4]
escolha = float(input("Digite sua opção (1/2/3/4): "))

if escolha in opcoes_validas: 

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    
    resultado = ''

    if escolha == 1: 
        resultado = num1 + num2
        print('O resultado da soma é: {}'.format(resultado))
    elif escolha == 2: 
        resultado = num1 - num2
        print('O resultado da subtração é: {}'.format(resultado))    
    elif escolha == 3:
        resultado = num1 * num2
        print('O resultado da multiplicação é: {}'.format(resultado))
    elif escolha == 4:
        if num2 != 0: 
            resultado = num1 / num2
            print('O resultado da divisão é: {}'.format(resultado))
        else: 
            print('Não é possível dividir por zero.')
else: 
    print('Escolha inválida. Escolha uma das opções 1/2/3/4.')