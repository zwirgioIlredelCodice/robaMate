import math

def raggruppamenti():
  tot = 0
  k=int(input("quanti gruppi vuoi inserire? "))
  for i in range(k):
    n=int(input("inserisci n: "))
    tot=tot*n
  print("il risultato è ",tot)


def disposizioni():
  tot = 0
  n=int(input("Inserisici il numero totale di elementi: "))
  k=int(input("Inserisci quanti elementi vuoi considerare: "))
  for i in range(0, k-1):
    tot=tot*n-i
  print("il risultato dell disposizione è ",tot)


def disposizioni_r():
  n=int(input("Inserisici il numero totale di elementi: "))
  k=int(input("Inserisci quanti elementi vuoi considerare:"))
  print("il risultato dell disposizione è ",n**k)


def permutazioni():
  tot = 0
  n=int(input("Inserisci il numero di elementi: "))
  tot=math.factorial(n)
  print("il risultato dell permutazione è ",tot)

def combinazione():
  n=int(input("Inserisci il numero di elementi: "))
  k=int(input("Inserisci il numero di elementi: "))
  nsom=1
  ksom=1
  nksom=1
  nsom=math.factorial(n)
  ksom=math.factorial(k)
  nksom=math.factorial(n-k)
  tot=nsom/(ksom*nksom)
  print("il risultato dell permutazione è ",tot)

def combinazioni_r():
  n=int(input("Inserisci il numero di elementi: "))
  k=int(input("Inserisci il numero di elementi: "))
  risultato = math.factorial((n+k-1))/(math.factorial(k)*math.factorial(n-1)) #https://www.youmath.it/lezioni/probabilita/calcolo-combinatorio/1217-combinazione-con-ripetizione.html
  print("il risultato dell permutazione è ",risultato)



