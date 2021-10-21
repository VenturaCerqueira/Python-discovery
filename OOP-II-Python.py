#Python Object-orieted Programming

#Classes
  #Utilizando para criar objetos ( instancias )
  #Objetos são partes dentro de uma Class ( Instancias)
  #Classes são utilizadas para agrupar dados e funções, podendo reutilizar
  #===
  # Class: Frutas
  # Objetos: abacate, banana...

#Criar a Class
class Funcionario:
  pass

#Criar objeto
usuario01 = Funcionario()
usuario02 = Funcionario()

#Criar os parametros do usuario 01
usuario01.nome ='Anderson'
usuario01.sobrenome = 'Ventura'
usuario01.data_nascimento = '21/05/2021'

#Criar os parametros do usuario 02
usuario02.nome ='Andre'
usuario02.sobrenome = 'Loiola'
usuario02.data_nascimento = '11/10/2021'

#Print
print(f'Nome completo:', usuario01.nome, usuario02.sobrenome, '\nData de nascimento: ', usuario01.data_nascimento)
print(f'Nome completo:', usuario02.nome, usuario02.sobrenome, '\nData de nascimento: ', usuario02.data_nascimento)