comprimento = float(input("Digite o comprimento da parede :"))
altura = float(input("Digite a altura da parede :"))

area = (comprimento * altura)
litro = (area / 3)
lata = (litro / 3.6)
valor = (lata * 107)

print("A área é de {}, quantidade de latas necessarias é de {}, valor gasto = {} : " .format ( area, lata, valor))