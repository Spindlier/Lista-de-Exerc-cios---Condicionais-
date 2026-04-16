numero = int(input("digite um número: "))

if numero == 0:
    print(f"O número {numero} é nulo, não vale")
elif numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f" o número {numero} é  impar")
