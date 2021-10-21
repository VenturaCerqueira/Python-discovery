try:
  valor = int(input('Digite o valor do seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar um valor em numeros!')
finally:
  print('Codigo Ok')

#else:
#  print('Uusuario digitou um valor correto')
 # resultado = valor * 2
 # print(resultado)