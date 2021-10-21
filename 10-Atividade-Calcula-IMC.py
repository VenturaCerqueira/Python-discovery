#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def calculaIMC(peso:float, altura:float):
  return float(peso/(altura*altura))


def css():
  print("------------------------------------")


css()
altura = float(input('Qual sua altura:\t'))
peso = float(input('Qual seu Peso:\t'))
css()
print(f'IMC:\t{calculaIMC(peso, altura):,.2f}')
css()