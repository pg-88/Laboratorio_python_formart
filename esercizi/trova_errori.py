## Qui trovate codice che non funziona bene
# l'obbiettivo è capire cosa non funziona e correggere opportunamente
# saper leggere codice di altri è molto importante ed è quasi più difficile
# che scriverlo
# Non sono in nessuun ordine particolare.

#--------------------------------- E S E R C I Z I O  1 ------------------------------
## IF statement
# controllo età: script che dovrebbe dirci in che fascia scolastica siamo 
# in funzione dell'età 
# errore di logica provate ad assegnare a eta i valori vicini ai vaolri limite

eta = 16

if eta < 1 or eta > 25:
    print("fuori età scolastica")
elif eta > 1 and eta <= 6:
    print("scuola dell'infanzia")
elif eta >= 6 and eta < 11:
    print("scuole elementari")
elif eta >= 11 and eta < 14:
    print("scuole medie")
elif eta >= 14 and eta < 19:
    print("scuole superiori")
elif eta >= 19 and eta <= 25:
    print("stai facendo l'università?")

#--------------------------------- E S E R C I Z I O  1 fine-----------------------------



#--------------------------------- E S E R C I Z I O  2 ------------------------------
# coordinate di un punto in un area
# #    Xmax  Ymax
area = [30, 30]
"""  _________________________
    |                         |
    |                         |
    |                         |
    |                         |
    |                         |
  y |    P                    |
    |     +                   |
    |                         |
    |                         |
    |_________________________|
  (0; 0)
                x
area parte dall'origine.
x rappresenta la dimensione massima orizzontale (base) 
y rappresenta la dimensione massima verticale (altezza)
x si trova richiamando area[0]
y si trova richiamando area[1]
"""
## definizione di un booleano, operatori di confronto
#     P(x=13; y=9)
punto = [13, 9]
interno_area = punto[0] > area[1] or punto[1] < area[0]
# la condizione è tutta sballata, correggere in modo che interno_area 
# sia True se e solo se il punto sta all'interno dell'area definita come sopra


#--------------------------------- E S E R C I Z I O  2 fine-----------------------------



#--------------------------------- E S E R C I Z I O  3 ------------------------------

#errori di tipo e sintassi

prezzo_latte = 7,99 # occhio a questa variabile!!! Fai un type(prezzo_latte) se non ti è chiaro

# if prezzo_latte > 1.00
#     print("inflazione galoppante")



#--------------------------------- E S E R C I Z I O  3 fine-----------------------------



#--------------------------------- E S E R C I Z I O  4 ------------------------------

# invertire l'ordine di valori in una lista 
tabellina_quattro = [prodotti for prodotti in range(0, 41, 4)] # list comprehension vedi slide 20 di Slide Laboratorio Python
print(tabellina_quattro)
al_contrario = []

for i in range(0, len(tabellina_quattro)):
    print("ciclo sull'elemento: ", tabellina_quattro[i])
    al_contrario.append(tabellina_quattro[i])
    print("la lista è a: ", al_contrario)

#ciclo terminato devo ottenere la lista da 40 a 0
print("ciclo finito: ", al_contrario)

# suggerimento: append accoda elementi alla lista, dovremmo riuscire a partire dall'ultimo
# quindi serve un range che parta dal massimo valore dell'indice e scenda fino a 0

#--------------------------------- E S E R C I Z I O  4 fine-----------------------------
