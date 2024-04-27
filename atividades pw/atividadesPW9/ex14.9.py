def operacao_completa(num1, num2):
    try:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    except ZeroDivisionError as e:
        # Tratamento específico para divisão por zero
        raise ValueError("Erro ao dividir:", e) from e
    except TypeError as e:
        # Tratamento específico para tipo de dado inadequado
        raise ValueError("Erro nos tipos de dados:", e) from None
    except Exception as e:
        # Tratamento genérico para outras exceções
        print("Erro inesperado:", e)
    finally:
        print("Operação concluída.")  # Ação a ser sempre executada, independentemente de exceções

# Exemplo de uso
try:
    operacao_completa(10, 0)
except ValueError as e:
    print("Erro:", e)
