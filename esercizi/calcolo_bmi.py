## Calcolare l'indice di massa corporea

# https://it.wikipedia.org/wiki/Indice_di_massa_corporea

def bmi(altezza, peso):
    """Calcola il BMI usando la formula peso corporeo diviso altezza al quadrato
    da un errore (o stampa un avviso) nel caso in cui uno o entrambe tra altezza e peso
    sia minore o uguale a zero.
    Rispettare i range indicati nella pagina https://it.wikipedia.org/wiki/Indice_di_massa_corporea
    Args:
        altezza: numero float rappresenta l'altezza in metri
        peso: numero float rappresenta la massa corporea in kg
    Return:
        ritorna una tra le seguenti stringhe: "Grave magrezza", "Sottopeso", "Leggermente sottopeso", "Regolare", "Sovrappeso", "Obesità di I classe", "Obesità di II classe", "Obesità di III classe"
        """
    pass


def test():
    """funzione di test"""
    if bmi(peso=62,altezza=1.7) == "Regolare":
        print("esercizio svolto correttamente")
    else:
        print("forse c'è qualcosa da sistemare")


test()
