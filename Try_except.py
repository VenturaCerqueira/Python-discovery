#Erros
  # Excelente para testes
  # Não realiza o 'Stop' no programa
  # Mensagens customizadas quando encontra um ArithmeticError

try:
  letras=['a', 'b', 'c']
  print(letras[3])
except IndexError:
  print('Index não existe')