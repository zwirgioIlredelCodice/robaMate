from combinatorio import*
while True:
  dec = input("Conta l'ordine? si/no: ")
  if dec== "si" or dec== "no":
    break
if dec=="si":
  while True:
    dec = input("sono presenti ripetizioni di stessi elementi?  si/no: ")
    if dec=="si" or dec=="no":
      break
  if dec == "no": 
    disposizioni()
  if dec=="si": 
    while True:
      dec = input("si possono ripetere tutti gli elementi?  si/no: ")
      if dec=="si" or dec=="no":
        break
    if dec=="si": 
      disposizioni_r()
    if dec=="no":
      permutazione_r()
elif dec=="no":   
    while True:
      dec = input("ci sono più elementi di certi insiemi che devi ragruppare in successione si/no: ")
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
