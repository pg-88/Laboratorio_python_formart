def gestione_input():
    """chiede input all'utente pulisce e controlla la stringa
    immessa dall'utente quindi invoca la funzione appropriata

    Arg:
        lista_operazioni: lista di stringhe che rappresentano
            le operazioni possibili"""
    operazione_scelta = input(
        "Scegli cosa fare:\noperazioni possibili sono addizione, conversione binario\nesci per terminare\n")  # termino con \n così il cursore va a capo
    while operazione_scelta != "esci":
        if operazione_scelta == "addizione":
            # la variabile res contiene il risultato dell'operazione
            res = operazione_addizione()
            print(res)
            print("la somma è: ", res)
        elif operazione_scelta == "conversione binario":
            # posso usare il nome res perché la variabile sopra è morta
            res = conversione_binario()
            print(res)
        elif operazione_scelta == "fattoriale":
            # fattoriale è il prodotto di tutti i numeri fino al numero indicato
            # 4! = 4 * 3 * 2 * 1
            # https://it.wikipedia.org/wiki/Fattoriale
            res = input_fattoriale()
            print("fattoriale", res)

        else:
            print("input non riconoscuto")
        operazione_scelta = input("Vuoi fare altri conti?\nAltrimenti esci per terminare\n")

#######################################  O P E R A Z I O N I  ##########################################################


def operazione_addizione():
    """chiede input di numeri separati da spazio
     e restituisce un numero che è la somma dei due input

    Return:
        numero int o float"""

    # chiedo input a utente lo metto nella variabile numeri_str
    numeri_str = input("Scrivi tutti gli addendi separati da uno spazio\n")  # sarà una stringa perché input torna sempre stringa

    # divido la stringa con il metodo split che crea una lista di stinghe
    numeri_lista = numeri_str.split()

    # print per vedere come funziona
    print("lista di stringhe che rappresentano gli addendi", numeri_lista)

    # variabile somma che viene usata dal ciclo per il totale finale
    somma = 0  # inizializzata al valore 0!!!

    for num in range(len(numeri_lista)):
        # trasformo ogni elemento della lista in float (int è un sottoinsieme di float)
        addendo = float(numeri_lista[num])  # bisognerebbe gestire eventuali errori!!!
        # aggiorno la variabile somma
        somma = somma + addendo
    print("finito il ciclo, la somma è:\n", somma)

    return somma


def conversione_binario():
    """prendere un numero come input e convertirlo a binario

    Return:
        stringa che rappresenta il numero in base 2
    """
    numero_str = input("Scrivi il numero da convertire\n")  # si possono comporre le chiamate di fz: `numero = int(input("Scrivi il numero da convertire\n")
    numero = int(numero_str)

    unita = numero % 10
    print(unita, unita // 2, unita % 2)

    numero_loop = numero  # variabile di appoggio per preservare la variabile numero
    stringa_num_bin = ""  # conterrà il risultato

    while numero_loop >= 1:
        stringa_num_bin = str(numero_loop % 2) + stringa_num_bin
        numero_loop = numero_loop // 2
        print("stringa", stringa_num_bin, "numero residuo", numero_loop)
    print("output", stringa_num_bin)
    return stringa_num_bin


def input_fattoriale():
    """gestisce l'input e invoca la funzione ricorsiva"""
    numero = int(input("Inserire il numero per calcolarne il prodotto fattoriale\n"))
    fatt = fattoriale(numero)
    return fatt


def fattoriale(num):
    """funzione ricorsiva ovvero richiama se stessa
    ogni volta l'argomento passato è sempre più piccolo,
    quando arriva a 1 le chiamate si chiudono e ritorna il risultato"""
    if num < 2:
        return 1
    else:
        return num * fattoriale(num - 1)

###########################################  S C R I T T U R A  L O G  #################################################


# richiamo la funzione gestione_input che fa partire tutto lo script
gestione_input()
