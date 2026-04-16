num1= float(input("digite uma nota: "))
num2 = float(input("digite outra nota: "))

nota_final = (num1+ num2) /2

if nota_final >=6:
    print(f"Aprovado!")
else:
    print("Reprovado!")