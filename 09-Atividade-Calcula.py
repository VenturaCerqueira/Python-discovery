#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a-o produto do dobro do primeiro com metade do segundo .
#B- Soma do triplo do primeiro com o terceiro.
#C- Terceiro elevado ao cubo.

#def  soma do triplo do primeiro com terceiro 
def soma_triplo_3(number01:int, number03:float):
  return (number01*3)+number03


#def soma dos numeros
def soma_total(number01:int , number02:int , number03:float ): 
  return (number01+number02+number03)


#def 3° ao cubo
def cubo(number03:float):
  return(number03*number03*number03)


#def dos "-"
def css():
  print('----------------------------------------------')


#recebe valores:
css()
number01 = int(input('Digite o primeiro numero:\t'))
css()
number02 = int(input('Digite o segundo numero:\t '))
css()
number03 = float(input('Digite numero Real:\t'))
css()
#Demonstra def
print(f'Total 1°+2°+3°:', soma_total(number01,number02, number03))
css()
print(f'Total da soma do triplo do 1° + 3°:', soma_triplo_3(number01, number03))
css()
print(f'O 3° valor ao cubo:', cubo(number03))
css()