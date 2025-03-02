nome = input("Digite seu nome: ")
salario = float(input ("Digite seu salário: "))
bonus = float(input ("Digite seu bônus: "))
CONSTANTE_BONUS = 1000

resultado = float((CONSTANTE_BONUS + salario) * bonus)

print (nome, "seu bônus de salário é:", resultado)

print (f" {nome} seu bônus de salário é:, {resultado}") # Outro jeito mencionado no video