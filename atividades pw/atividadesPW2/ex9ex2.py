data = input("Digite uma data válida no formato dd/mm/aaaa: ")

try:
    dia, mes, ano = map(int, data.split("/"))
    if 1 <= dia <= 31 and 1 <= mes <= 12:
        if mes == 2:
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                if not 1 <= dia <= 29:
                    raise ValueError
            elif not 1 <= dia <= 28:
                raise ValueError
        elif mes in [4, 6, 9, 11]:
            if not 1 <= dia <= 30:
                raise ValueError
    else:
        raise ValueError

    print("Data válida:", data)
except (ValueError, IndexError):
    print("Data inválida. Por favor, insira uma data válida no formato dd/mm/aaaa.")
