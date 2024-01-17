"""Esercizi sulle classi"""

"""
 1) Libro - Biblioteca:
    definire 2 classi, una si chiama Libro e l'altra Biblioteca.
    Libro deve contenere almeno 3 proprietà (se volete potete inserirne di nuove ma il minimo sono queste 3):
        - Titolo: stringa
        - Autore: stringa
        - disponibile: booleano
    il costruttore assegnerà automaticamente il valore True alla proprietà 'disponibile'
    Inoltre la classe deve avere anche un metodo che si occupa di cambiare il valore
    di 'disponibile' da True a False e viceversa

    Biblioteca avrà solamente una proprietà (lista_libri o elenco_libri) che sarà appunto una lista 
    di tutti i libri (gli oggetti creati con la classe Libro).
    Il costruttore prenderà come parametro una lista di libri o una lista vuota.
    La classe avrà poi alcuni metodi:
        - conta libri: restituisce il numero di libri che appartengono alla biblioteca (sia disponibili che non)
        - libri disponibili: restituisce la lista dei soli libri disponibili in questo momento
        - libri in prestito: restituisce una lista di libri che non sono disponibili al momento
        - aggiungi libro: crea un oggetto libro e lo inserisce in lista
        - rimuovi libro: individua un libro presente e lo rimuove dalla lista

    Sotto la struttura di base delle 2 classi:
"""

class Libro:
    
    def __init__(self, titolo, autore) -> None:
        pass

    def toggleDisponibile(self):
        pass


class Biblioteca:

    def __init__(self, libri_list: list) -> None:
        pass

    def contaLibri(self) -> int:
        pass

    def disponibili(self) -> list:
        pass

    def prestati(self) -> list:
        pass

    def aggiungiLibro(self, titolo: str, autore: str) -> None:
        pass

    def rimuoviLibro(self, titolo: str, autore: str) -> None:
        pass
