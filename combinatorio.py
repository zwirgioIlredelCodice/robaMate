import math

def input_n():
  n = 0
  while n <= 0 or n > 500:
    n = int(input("immetti n > 0 e < 500: "))
  return n

def input_k():
  k = 0
  while k <= 0 or k > 500:
    k = int(input("immetti k > 0 e < 500: "))
  return k


def raggruppamenti():
  tot = 1
  k=int(input("quanti gruppi vuoi inserire? "))
  for i in range(k):
    n=int(input("inserisci n: "))
    tot=tot*n
  print("il risultato è ",tot)


def disposizioni():
  tot = 1
  while True:
    n=input_n()
    k=input_k()
    if k<n+1:
      break
  for i in range(k):
    tot=tot*(n-i)
  print("il risultato dell disposizione è ",tot)


def disposizioni_r():
  n=input_n()
  k=input_k()
  print("il risultato dell disposizione è ",n**k)


def permutazioni():
  tot = 0
  n=input_n()
  tot=math.factorial(n)
  print("il risultato dell permutazione è ",tot)

def permutazione_r():
  tot = 0
  n=input_n()
  ripetuti = []
  n_ripetuti = int(input("quanti sono gli elementi ripetuti?"))
  

  print("il risultato dell permutazione è ",tot)


def combinazione():
  while True:
    n=input_n()
    k=input_k()
    if k<n:
      break
    else:
      print("k deve essere minore di n")
  tot=math.factorial(n)/(math.factorial(k)*math.factorial((n-k)))
  print("il risultato dell permutazione è ",tot)

def combinazioni_r():
  n=input_n()
  k=input_k()
  risultato = math.factorial((n+k-1))/(math.factorial(k)*math.factorial(n-1)) #https://www.youmath.it/lezioni/probabilita/calcolo-combinatorio/1217-combinazione-con-ripetizione.html
  print("il risultato dell permutazione è ",risultato)



