try:
    # código onde você espera que uma exceção possa ocorrer
    # se ocorrer uma exceção aqui, o fluxo do programa será desviado para o bloco except
except Excecao1:
    # código a ser executado se a Excecao1 for levantada no bloco try
except Excecao2 as variavel:
    # código a ser executado se a Excecao2 for levantada no bloco try,
    # e a exceção é capturada e atribuída à variável
except:
    # código a ser executado se qualquer outra exceção for levantada no bloco try
else:
    # código a ser executado se nenhuma exceção for levantada no bloco try
finally:
    # código a ser sempre executado, independentemente de uma exceção ser levantada ou não
