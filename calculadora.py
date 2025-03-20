import time

def obter_operacao():
    print("Escolha uma das operações de acordo com seu numero:")
    print("1.Soma")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5.Potenciação")
    print("6.Raiz")

    while True:
        try:
            nota = int(input(f"Digite o numero da operação desejada: "))
            if 0 <= nota <= 6:
                return nota
            else:
                print("Operação invalida")
        except ValueError:
            print("Entrata Invalida")   

def obter_valor(valor):
    while True:
        try:
            nota = float(input(f"Digite o valor{valor}: "))
            return nota
        except ValueError:
            print("Entrata Invalida")   

def calcular_operacao():
    operacao_num = obter_operacao()

    if operacao_num == 1:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 + valor2)
        print(f"O resultado da Soma é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()

    elif operacao_num == 2:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 - valor2)
        print(f"O resultado da Subtração é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()

    elif operacao_num == 3:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 * valor2)
        print(f"O resultado da Multiplicação é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()    

    elif operacao_num == 4:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 / valor2)
        print(f"O resultado da Divisão é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()    

    elif operacao_num == 5:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 ** valor2)
        print(f"O resultado da Potencia é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()   

    elif operacao_num == 6:
        valor1 = obter_valor(1)
        valor2 = obter_valor(2)
        resultado = int(valor1 **(1/valor2))
        print(f"O resultado da Raiz é: {resultado}")
        time.sleep(1.5)
        calcular_operacao()              

calcular_operacao()



