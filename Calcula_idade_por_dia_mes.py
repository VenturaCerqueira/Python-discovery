#calcula idade
dia_nasc  = int(input("Digite o dia de nascimento:\t"))
mes_nasc  = int(input("Digite o mês de nascimento:\t"))
ano_nasc  = int(input('Digite o ano do nascimento:\t'))
print(f'Sua data de nascimento é', dia_nasc, '/', mes_nasc, "/", ano_nasc, ".")

print('Loading...')

#....
dia_atual = int(input("Digite o dia que se encontra:\t "))
mes_atual = int(input("Digite o mês que se encontra:\t"))
ano_atual = int(input('Digite o ano que se encontra:\t'))
print(f'Hoje:', dia_atual, '/', mes_atual, '/', ano_atual, '.')

print('Loading...')

#calculando idade
if mes_nasc == mes_atual:
  
  if dia_nasc > dia_atual:
    idade = (ano_atual - ano_nasc)-1
    print(f'Sua idade é:', idade)

  elif dia_nasc == dia_atual:
    idade = ano_atual - ano_nasc
    print(f'Parabens, Hoje e seu aniversario, bolo, guarana e muita festa para você!!!')
    print(f'Sua idade é:', idade)
    print(f'Ta ficando mais velho ehm.. kkkk')

  else:
   idade = ano_atual - ano_nasc
   print(f'Sua idade é:', idade)

elif mes_nasc > mes_atual:
  print("Loading...")
  idade = (ano_atual - ano_nasc)-1
  print(f'Sua idade é:', idade)

else:
  idade = ano_atual - ano_nasc
  print(f'Sua idade é:', idade)




