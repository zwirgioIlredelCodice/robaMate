from combinatorio import*
while True:
  dec = input("Conta l'ordine? si/no: ")
  if dec== "si" or dec== "no":
    break
if dec=="si":
  while True:
    dec = input("sono presenti ripetizioni?  si/no: ")
    if dec=="si" or dec=="no":
      break
  if dec == "no": 
    disposizioni()
  if dec=="si": 
    while True:
      dec = input("c'è almeno un elemento uguale ad un altro?  si/no: ")
      if dec=="si" or dec=="no":
        break
    if dec=="si": 
      permutazione_r()
    if dec=="no":
      disposizioni_r()
elif dec=="no":   
    while True:
      dec = input("ci sono più elementi di certi insiemi che puoi ragruppare in successione ; devi associare degli elementi di un gruppo d un altro? si/no: ")
      if dec=="si" or dec=="no":
        break
    if dec=="si":
      raggruppamenti()
    if dec=="no":
      while True:
        dec = input("possono esserci ripetizioni? si/no: ")
        if dec=="si" or dec=="no":
          break
      if dec=="si":
        combinazioni_r()
      if dec=="no":
        combinazione()
    

    

