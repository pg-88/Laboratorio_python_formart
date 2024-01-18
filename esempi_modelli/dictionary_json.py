import json
#alternativa per l'import 
# from json import load, dump

utenti = json.load(open("./risorse/test.json"))
print(utenti, type(utenti))

json.dump(utenti, open("./risorse/nuovi_utenti.json")) # attenzione al flag di apertura del file 