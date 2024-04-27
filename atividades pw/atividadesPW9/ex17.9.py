import asyncio

async def minha_corrotina():
    try:
        # Código que pode gerar uma exceção assíncrona
        resultado = await alguma_operacao_assincrona()
    except AlgumaExcecaoAssincrona as e:
        # Tratamento da exceção assíncrona
        print("Erro assíncrono:", e)
    finally:
        # Código a ser executado sempre, independentemente de exceções
        print("Corrotina concluída.")

async def alguma_operacao_assincrona():
    # Simulando uma operação assíncrona
    await asyncio.sleep(1)
    # Simulando uma exceção assíncrona
    raise ValueError("Erro durante operação assíncrona.")

# Exemplo de uso
asyncio.run(minha_corrotina())

