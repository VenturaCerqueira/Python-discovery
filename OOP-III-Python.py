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
  
  def __init__(self, nome, sobrenome, data_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.data_nascimento = data_nascimento

#Criar objeto
usuario01 = Funcionario('Anderson', 'Ventura', '21/05/1999')
usuario02 = Funcionario('Carol', 'Silva', '12/10/2000')

#Print
print(usuario01.nome)
print(usuario02.nome)

#Criar os parametros do usuario 01
#usuario01.nome ='Anderson'
#usuario01.sobrenome = 'Ventura'
#usuario01.data_nascimento = '21/05/2021'

#Criar os parametros do usuario 02
#usuario02.nome ='Andre'
#usuario02.sobrenome = 'Loiola'
#usuario02.data_nascimento = '11/10/2021'