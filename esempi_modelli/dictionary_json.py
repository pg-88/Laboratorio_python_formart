import json
#alternativa per l'import 
# from json import load, dump

utenti = json.load(open("./risorse/test.json"))
print(utenti, type(utenti), utenti["datiUtenti"])

json.dump(utenti, open("./risorse/nuovi_utenti.json", 'w')) # attenzione al flag di apertura del file
