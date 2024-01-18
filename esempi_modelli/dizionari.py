"""Struttura di dati key-value"""

# esempio semplice
persona = {
    "nome": "Mario",
    "cognome": "Rossi",
    "altezza": 1.79
}

# richiamare i valori
print(f"Ho conosciuto {persona['nome']} {persona['cognome']}, è alto {persona['altezza']}")

# cicli con i dictionary
#  - brutalmente
for i in persona:
    print(i)

#  - ciclando sui valori
for i in persona.values():
    print(i)

#  - con 2 indici contemporaneamente
for k, v in persona.items():
    print("chiave ", k, "valore ", v)

#  dictionary comprehension
tabellina_tre = { v: v*3 for v in range(11) }
print(tabellina_tre)

# Quante liste servono per fare un dictionary?
# funzione nativa zip()
chiave = [f"nome{i + 1}" for i in range(3)] 
print(chiave)
valore = ["Maria", "Sara", "Sofia"]
print(dict(zip(chiave, valore)))

pranzo = {
    "antipasto": "sarde in saor e polenta",
    "primo": "bigoli all'anatra",
    "secondo": "spezzatino e polenta",
    "contorno": "insalatina",
    "dolce": "tiramisù",
    "conclusione": "caffé e ammazza caffé"
}

lista_spesa = {
    1: "ciambelle",
    2: "batterie",
    3: "caffé",
    4: "caffé",
    5: "caffé"
}