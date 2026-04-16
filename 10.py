peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Baixo peso")
elif imc < 25:
    print(f"IMC: {imc:.2f} - Normal")
elif imc < 30:
    print(f"IMC: {imc:.2f} - Sobrepeso")
else:
    print(f"IMC: {imc:.2f} - Obesidade")