#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# função que converte Temperatura Fahrenheit para celsius:
def celsius(Fah_temp):
  return (Fah_temp-32)/1.8  #(°F − 32) ÷ 1, 8 = C°


Fah_temp = float(input('Temperatura F°:\t'))
print('\n', celsius(Fah_temp))