#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

not01 = float(input('Digite a primeira nota: '))
not02 = float(input('Digite a segunda nota : '))
not03 = float(input('Digite a terceira nota :'))
not04 = float(input('Digite a quarta nota: '))

def calcula_media():
  return f'{float((not01+not02+not03+not04)/4)} média dentra as notas'
 
print(calcula_media())