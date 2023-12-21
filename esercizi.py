# Spunti per esercizi da sviluppare o completare in autonomia

#Es 1 - conversione in numero binario

#serve un intero!
num_dec = 42 # base 10

#per semplicità uso una lista o volendo una stringa
#comunque una struttura dati manipolabile
num_bin = ""

# l'idea è quella di iterare più volte andando a "consumare" il numero in base
# 10 per popolare il numero binario

# matematicamente:
# 42 = 
# 1,   2,    4,     8,     16,   32,    64,   128,   256,   512  base 10
# 
# 2^0  2^1   2^2    2^3    2^4   2^5    2^6   2^7    2^8    2^9  potenze di 2
#  
#  0    1     0      1      0     1  
# quindi 42 è 101010  ovvero 2^1 + 2^3 + 2^5

num_loop = num_dec # nuova variabile per preservare il numero originale

# while num_loop >= 0:
#     print(num_loop % 10) # estrapolo l'ultima cifra
#     num_loop = num_loop // 2
#     print(num_loop)

print(f"il numero {num_dec} in base 2 è {num_bin}")


# Es 2 - Dividere Stringhe e contare parole

stringa_lunga = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# usare il metodo stringa_lunga.split() per dividere la stringa ad ogni spazio

# usare la funzione len(stringa_lunga) per contare quante "parole" sono contenute

# Es 2.1 - Contare quante volte appare la parola 'dolor'

# ciclare la lista generata dallo .split() nel blocco del ciclo for
# con un if controllare quando la stringa coincide con 'dolor'


# Es 3 - Diversi split

# come dividere una stringa quando non ci sono spazi ma altri caratteri?
# Esempio
stringa_under = "qui_non_ci_sono_spazi_ma_voglio_comunque_separare_con_split"

# Es 4 - Serie di input dall'utente e "pulizia dell'input"

# fare ciclo while per chiedere un input e prima di controllare la stringa
# ripulirla togliendo spazi e facendo in modo che sia tutto maiuscolo o tutto 
# minuscolo.

# L'obiettivo è che l'utente non si debba preoccupare di maiuscole e minuscole
# o degli spazi ma sia libero di dare l'input come preferisce

# Condizione di uscita dal ciclo è la stringa 'quit' oppure 'esci' oppure 'q'
# attenzione alla condizione di uscita per non incappare in loop infiniti

input_utente = input("""
Seleziona un'operazione,
le possibilità sono:
 - uno
 - due
 - tre
 - quattro 
 - altro
quit o q o esci per uscire.""")

input_pulito = "" # = nell'input_pulito inseriamo il valore dell'input dopo aver sistemato la stringa

# while : # condizione su input_pulito per verificare se è 'quit' oppure 'esci' oppure 'q' 
#     pass
#     # eliminare pass e completare il blocco del ciclo

def funzione_con_parametri_esempio(numero):
    if numero != 0: 
        print("siamo nella funzione esempio")
    for i in range(10):
        print("#" * i)


matricola = 10
funzione_con_parametri_esempio(matricola)

def funzione_saluti(nome):
    if nome:
        return "hello " + nome + '!'
    # si poteva anche comporre la stringa con f"hello {nome}!"
    else: 
        print("manca il nome")


funzione_saluti('')
funzione_saluti('pietro')
saluta_me = funzione_saluti("Pietro")
print(saluta_me)

def mando_saluti():
    return "Hello World!"