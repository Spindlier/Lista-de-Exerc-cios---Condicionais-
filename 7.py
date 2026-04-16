salario = float(input("Digite seu salário: "))

if salario > 5000:
    desconto = salario * 0.10
    novo_salario = salario - desconto
    print(f"O desconto será de R$ {desconto:.2f}. E seu novo salário será: R$ {novo_salario:.2f}")
else:
    desconto = salario * 0.05
    novo_salario = salario - desconto
    print(f"O desconto será de R$ {desconto:.2f}. E seu novo salário será: R$ {novo_salario:.2f}")