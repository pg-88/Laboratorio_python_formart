# user_select = input("Ciao, Facciamo un po di conti?")

# if user_select == "addizione":
#     # input mi permette di raccogliere l'input dell'utente come STRINGA
#     addendi = input("dammi i numeri uno dopo l'altro")
#     # trasformare addendi in numeri
# elif user_select == "moltiplicazione":
#     # elif permette di controllare una ulteriore condizione nel caso non si entri nel primo blocco true
#     fattori = input("dammi due numeri")
# else:
#     raise Exception("Nessuna selezione valida")


lista_mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
linguaggi = ["python", "C", "C++", "cobol", "javascript"]

numeri_belli = [3.14, 42, 360]

lista_mista = [90, "la paura", 77, "le gambe delle donne", 42, "il senso della vita l'universo e tutto quanto"]

print(lista_mesi[1:4])  # nome variabile che contiene la lista e indice tra quadre

for i in range(0, 100, 1):
    print(i)

for i in range(0, len(lista_mesi), 1):
    print(f"mese {lista_mesi[i]} anno 2023")
else:
    print("sono finiti i mesi")

for i in lista_mesi:
    print(i)

tabellina_tre = [num for num in range(0, 500, 3)]
# print(tabellina_tre)

for t in range(0, len(tabellina_tre)):
    print(f"3 moltiplicato per {t} è uguale a {tabellina_tre[t]}")

multipli_tre_pari = [num for num in range(0, 300, 3) if num % 2 == 0]
print("i multipli di 3 pari, tra 0 e 300 sono: ", multipli_tre_pari)
