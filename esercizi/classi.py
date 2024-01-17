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

    Una volta fatto tutto quanto indicato sopra, come extra potete provare a gestire le date di prestito e rientro

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

"""
2) Persona: 
    classe che raccoglie i dati di una persona:
    - nome
    - cognome
    - altezza
    - peso
    metodi per aggiornare peso e altezza (potrebbe essere un bambino in fase di crescita)
    metodo per il calcolo del bmi
    ** Extra annotare in un file di testo tutti gli oggetti persona che vengono creati
    (suggerimento nel costruttore apriamo un file e scriviamo le stesse stringhe che servono a creare le proprietà della classe)

"""
class Persona:
    
    def __init__(self, nome: str, cognome: str, peso: float, altezza: float) -> None:
        pass

    def set_peso(self, nuovo_peso: float) -> None:
        pass

    def set_altezza(self, nuova_altezza: float) -> None:
        pass
