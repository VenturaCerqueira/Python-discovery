
#lista extend
produtos =['Arroz', 'Feijão', 'Laranja', 'Banana', 5, 6, 7, 8]

#item1, item2, item3, item4 = produtos

#print(f'{item1}, {item2}, {item3} e {item4}.')

item1, item2, item3, *outros = produtos

print(f'{item1}, {item2} e {item3}.')

print(outros)


valores = 50, 80, 110, 150, 170

for x in valores:
  print(f'O valor final do produto é de R$: {float(x):.2f}.')
