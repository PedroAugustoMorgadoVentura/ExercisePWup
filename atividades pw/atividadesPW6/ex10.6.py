import tkinter as tk

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calcular_fibonacci():
    n = int(entrada_numero.get())
    resultado = fibonacci(n)
    resultado_label.config(text=f"O {n}° termo da sequência de Fibonacci é {resultado}")

# Configurações da janela
janela = tk.Tk()
janela.title("Calculadora Fibonacci")

# Frame principal
frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack()

# Entrada para o número de termos
label_numero = tk.Label(frame_principal, text="Digite o valor de n:")
label_numero.grid(row=0, column=0)

entrada_numero = tk.Entry(frame_principal)
entrada_numero.grid(row=0, column=1)

# Botão para calcular
botao_calcular = tk.Button(frame_principal, text="Calcular", command=calcular_fibonacci)
botao_calcular.grid(row=1, columnspan=2)

# Exibição do resultado
resultado_label = tk.Label(frame_principal, text="")
resultado_label.grid(row=2, columnspan=2)

# Execução da janela
janela.mainloop()
