def dividir_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Certifique-se de digitar números válidos.")
    finally:
        print("O bloco 'finally' foi executado.")
        # Aqui você pode colocar código para limpar recursos ou realizar ações de limpeza

dividir_numeros()
