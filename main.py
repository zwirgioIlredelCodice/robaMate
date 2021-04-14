from combinatorio import*
mol=1
while True:
  dec = input("Conta l'ordine? si/no")
  if dec== "si" or dec== "no":
    break

if dec=="si":
  dec = input("è già suddiviso in gruppi?  si/no")

  while True:
    dec=input("")
    if dec=="si" or dec=="no":
      break

  if dec=="si": #raggruppamenti
    break
   
  
  if dec == "no": #3
    dec = input("k = n?  si/no")
    while True:
      dec=input("")
      if dec=="si" or dec=="no":
        break

    while True:
      dec=input("")
      if dec=="si" or dec=="no":
        break

    if dec == "si": #4
      dec = input("si può ripetere?  si/no")

      while True:
        dec=input("")
        if dec=="si" or dec=="no":
          break
      
      if dec == "si":#5 disposizioni con ripetizioni
        #disposizioni con ripetizioni
      
      if dec == "no": #6
        #disposizioni
      else:
        print("risposta non valida")

    elif dec = "no": #7
      dec = input("si può ripetere?  si/no")

      while True:
        dec=input("")
        if dec=="si" or dec=="no"
          break
      if dec = "si":#8
        #permutazioni con ripetizioni
      
      elif dec == "no": #9
        #permutazione
      
      
    
    
elif dec == "no": #10
  dec = input("si può ripetere?  si/no")

  while True:
      dec=input("")
      if dec=="si" or dec=="no"
        break
  if dec = "si":#11
      #permutazioni con ripetizioni
     elif dec == "no": #10
      #combinazione semplice
  
    


