
class Credenziali:
    """Gestisce le credenziali di un utente"""

    def __init__(self, username, password) -> None:
        """inizializza password e username
        
        Args:
            username: stringa
            password: stringa 
        """
        self.__password = password  # attributo privato (perché dichiarato con '__' davanti al nome)
        self.__username = username  # attributo privato (perché dichiarato con '__' davanti al nome)

    def accedi(self, user, psw) -> bool:
        """torna true se abbiamo il permesso di accedere, altrimenti false"""
        return self.__username == user and self.__password == psw

    def aggiorna_psw(self, nuova_psw, vecchia_password) -> None:        
        """controlla che la vecchia psw sia giusta quindi riassegna la nuova password
        
        Args: 
            nuova_psw: stringa
            vecchia_psw: deve coincidere con quella in memoria"""
        
        if vecchia_password == self.__password:
            self.__password = nuova_psw
            print("La password è stata cambiata")


## Esempio di uso della classe
credenziali_user = Credenziali("utente", "1234!")

## 
from Modulo import funzione_del_modulo