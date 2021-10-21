#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#Calculo da rea e : A :Pi * R²
PI = float(3.14)
raio = float(input('Digite o raio do círculo: '))

def area():
  return f' A rea total do círculo e : {float(PI*(raio*raio))}'


print(area())