#raggruppamenti

k=int(input("inserisci quanti gruppi vuoi inserire: ))
for i in range(0, k):
  n=int(input("inserisci n: "))
  tot=tot*n
print(tot)

#disposizioni
n=int(input("Inserisici il numero totale di elementi: ))
k=int(input("Inserisci quanti elementi vuoi considerare:))
for i in range(0, k-1):
  tot=tot*n-i
print(tot)

#disposizioni con ripetizioni
n=int(input("Inserisici il numero totale di elementi: ))
k=int(input("Inserisci quanti elementi vuoi considerare:))
print(n**k)

#permutazioni
n=int(input("Inserisci il numero di elementi))
for i in range(0, n-1):
  tot=tot*(n-i)
print(tot)