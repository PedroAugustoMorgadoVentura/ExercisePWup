import cmath
print("Insira o primeiro número complexo:")
real_part_1 = float(input("Parte real: "))
imag_part_1 = float(input("Parte imaginária: "))
numero_complexo_1 = complex(real_part_1, imag_part_1)
print("\nInsira o segundo número complexo:")
real_part_2 = float(input("Parte real: "))
imag_part_2 = float(input("Parte imaginária: "))
numero_complexo_2 = complex(real_part_2, imag_part_2)
soma = numero_complexo_1 + numero_complexo_2
produto = numero_complexo_1 * numero_complexo_2
print("\nSoma dos números complexos:", soma)
print("Produto dos números complexos:", produto)
