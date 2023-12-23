def gestione_input():
    """chiede input all'utente pulisce e controlla la stringa
    immessa dall'utente quindi invoca la funzione appropriata

    Arg:
        lista_operazioni: lista di stringhe che rappresentano
            le operazioni possibili"""
    operazione_scelta = input(
        "Scegli cosa fare:\noperazioni possibili sono addizione, conversione binario\nesci per terminare")
    while operazione_scelta != "esci":
        if operazione_scelta == "addizione":
            res = operazione_addizione()
            print("la somma è: ", res)
        elif operazione_scelta == "conversione binario":
            res = conversione_binario()

        else:
            print("input non riconoscuto")
        operazione_scelta = input("Vuoi fare altri conti?\nAltrimenti esci per terminare")


def operazione_addizione(*addendi):
    """chiede input di due numeri e restituisce un numero che è
    la somma dei due input

    Return:
        numero int o float"""
    print("2+2=4")


def conversione_binario():
    """prendere un numero come input e convertirlo a binario

    Return:
    """
    pass


gestione_input()