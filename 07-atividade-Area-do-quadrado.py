#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
quad = float(input('Digite o valor de um lado do quadrado: '))

def calc_quad():
  return f'O valor da area do quadrado é : {(quad*quad)*2}'

print(calc_quad())