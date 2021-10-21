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

  def nome_completo(self):
    return self.nome + ' '+self.sobrenome

#Criar objeto
usuario01 = Funcionario('Anderson', 'Ventura', '21/05/1999')
usuario02 = Funcionario('Carol', 'Silva', '12/10/2000')

#Print
print(usuario01.nome_completo())
print(Funcionario.nome_completo(usuario01))


