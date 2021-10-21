#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
def css():
  print("--------------------------------------------")


css()
nome = str(input('Nome:\t'))
css()
h = float(input('Altura:\t'))#altura
css()
peso = float(input('Peso:\t'))
css()
sex = input('Sexo M/F:\t')
css()

def calculaIMC(peso:float, h:float):
  return float(peso/(h**2))


if sex=='M'or sex=='Masculino' or sex=='m':
  def calcula_sex_Masc(h:float):
    return float((72.2*h)-58)


  import os #Limpa tela
  os.system('clear') or None
  
  css()
  print(f'Seu IMC {nome} :\t {calculaIMC(peso,h):.2f}')
  print(f'Peso idela para você {nome}:\t {calcula_sex_Masc(h):.2f}')
  css()
 

if sex =='F' or sex =='Feminino' or sex =='f' or sex =='feminino':
  def calcula_sex_fem(h:float):
    return float((62.1*h)-44.7)


  import os #Limpa tela
  os.system('clear') or None
  
  css()
  print(f'Dados de calculo de {nome} :')
  print('')
  print(f'Seu IMC {nome} :\t {calculaIMC(peso,h):.2f}')
  print(f'Peso ideal para você {nome}:\t{calcula_sex_fem(h):.2f}')
  print('')
  css()
 

