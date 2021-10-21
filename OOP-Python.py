#Python Object-orieted Programming

#Classes
  #Utilizando para criar objetos ( instancias )
  #Objetos são partes dentro de uma Class ( Instancias)
  #Classes são utilizadas para agrupar dados e funções, podendo reutilizar
  #===
  # Class: Frutas
  # Objetos: abacate, banana...
class Funcionarios:
  nome = 'Anderson'
  Sobrenome = 'Ventura'
  Data_nascimento = '21/05/2021'
Usuario1 = Funcionarios()
print(f'Nome completo:', Usuario1.nome, Usuario1.Sobrenome,  '\nData de nascimento:',  Usuario1.Data_nascimento)