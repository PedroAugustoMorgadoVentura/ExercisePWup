import sys
def executararquivo(nomearquivo):
    try:
        with open(nomearquivo, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nomearquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro: Ocorreu um problema ao ler o arquivo '{nomearquivo}': {e}")

def main():
    nomearquivo = input("Insira o nome do arquivo: ")
    executararquivo(nomearquivo)

if __name__ == "__main__":
    main()
