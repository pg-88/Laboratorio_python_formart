input_utente = input("""
Seleziona un'operazione,
le possibilità sono:
 - uno
 - due
 - tre
 - quattro 
 - altro
quit o q o esci per uscire.""")

input_pulito = input_utente.strip()
input_pulito = input_pulito.lower()

while not (input_pulito == 'q' or input_pulito == 'esci' or input_pulito == 'quit'):

    if input_pulito == 'uno':
        print("eseguire blocco uno")
    elif input_pulito == 'due':
        print("eseguire blocco due")
    elif input_pulito == 'tre':
        print("eseguire blocco tre")
    elif input_pulito == 'quattro':
        print("eseguire blocco quattro")
    elif input_pulito == 'altro':
        print("eseguire blocco altro")
    else: 
        print("la stringa immessa non coincide con nessuna possibilità\nRiprova")

    input_utente = input("Dammi un'altra operazione:\n")
    input_pulito = input_utente.strip()
    input_pulito = input_pulito.lower()


