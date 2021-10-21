# GERA A SEQUÊNCIA DE FIBONACCI OU A GENERALIZADA USANDO A REGRA DE FIBONACCI
import math # Ativa o módulo de funções matemáticas
""" Usa a regra de Fibonacci (cada elemento é a soma dos dois anteriores)
    para gerar uma sequência de N números de Fibonacci ou de números positivos
    ou negativos (um dos dois iniciais deve ser diferente de zero) e a razão entre cada dois
    elementos consecutivos; estes ultrapassarem 999 haverá perda do alinhamento dos resultados."""
print('Deseja a sequência de Fibonacci (F) ou uma qualquer (Q)?')
Resposta='X'
# Verifica se a resposta foi F ou Q, senão insiste
while Resposta != 'F' and Resposta != 'Q':
   Resposta=input('Digite F ou Q: ')
   if Resposta == 'F':
      FibA = 1
      FibB = 1
   elif Resposta == 'Q':
     while True:
        FibA = int(input('Entre com o primeiro número: '))
        FibB = int(input('Entre com o segundo número: '))
        if FibA == 0 and FibB == 0:
          print('Um deles deve ser diferente de zero!')
        else: break
while True:
   Ult=int(input('Entre com o número de elementos: '))
   if Ult <=1:
      print('O número de elementos deve ser >= 2!')
   else: break    
# Imprime os títulos da tabela
if Resposta == 'F':
   print(' N Fib(N) Razão')
else: print(' N Qquer(N) Razão')
# Imprime os dois primeiros elementos
if Resposta == 'F':
   print ('001 001')
   print ('002 001 1.0')
else: # Resposta foi Q
# Imprime os dois primeiros elementos
 if Resposta == 'F':
   print ('001 001')
   print ('002 001 1.0')
 else: # Resposta foi Q
  if FibA>=0:
     print('001', '00'+str(FibA) if FibA<10 else '0'+str(FibA) if FibA<100 else FibA)
  else: print('001 ' ,'-00'+str(abs(FibA)) if abs(FibA)<10 else '-0'+str(abs(FibA)) if
     abs(FibA)<100 else FibA)
if FibB>=0:
   print('002', '00'+str(FibB) if FibB<10 else '0'+str(FibB) if FibB<100 else FibB,
   FibB/FibA if FibA != 0 else " ") # evita a divisão por 0
else: print('002' ,'-00'+str(abs(FibB)) if abs(FibB)<10 else '-0'+str(abs(FibB))
      if abs(FibB)<100 else FibB, FibB/FibA if FibA!=0 else " ") # evita a
      #Gera a sequência a partir do 3o. elementeo
for N in range (1, Ult+1): #gera uma linha enquanto até o último elemento
   Aux = FibA + FibB # Cada novo elemento será a soma dos dois anteriores
   FibA = FibB # O segundo elemento torna-se o primeiro
   FibB = Aux # O segundo elemento recebe a soma dos dois anteriores
   # Concatena um 00 à esquerda se Fib(N) for menor do que 10
   # e 0 se for maior do que 9 e menor do que 100 inserindo - se for negativo
   if FibB>0:
     print('00'+str(N) if N<10 else '0'+str(N) if N<100 else N,
     '00'+str(FibB) if FibB<10 else
     '0'+str(FibB) if FibB<100 else FibB, FibB/FibA if FibA != 0 else " ")
   else: print('00'+str(N) if N<10 else '0'+str(N) if N<100 else N,
     '-00'+str(abs(FibB)) if abs(FibB)<10 else
     '-0'+str(abs(FibB)) if abs(FibB)<100 else FibB, FibB/FibA if FibA!=0 else " ")
RazAu = (1+math.sqrt(5))/2 #Razão Áurea
print('Compare com a razão áurea:\n','      '+str(RazAu)if FibB>0 else ' '+str(RazAu))

