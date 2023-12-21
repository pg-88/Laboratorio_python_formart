######################## NOTE OPERATIVE SULLE FUNZIONI ########################

#Dopo la definizione della funzione, è sempre bene mettere un commento per 
# spiegare cos'è e cosa dovrebbe fare la funzione
#ESEMPIO - funzione inutile a livello pratico ma mette in evidenza come
#commentare in modo che si capisca il comportamento e come usare la fz

def controllo_credenziali(nome, password):
    """chiede input nome e password e li controlla con quelli passati alla 
    funzione

    Args:
        nome: stringa, il nome utente corretto
        password: stringa, la password corretta 
    Return: 
        Nome e password come tupla, se corretti, 
        tupla vuota altrimenti
    """
    input_nome = input("Inserisci il nome utente")
    input_nome = input_nome.strip()  # elimina eventuali spazi accidentali

    input_psw = input("Inserisci password")
    input_psw = input_psw.strip()  # elimina eventuali spazi accidentali

    if nome == input_nome and password == input_psw:
        print("Credenziali corrette")
        return (input_nome, input_psw)
    else: 
        return()

## Es 1 
# definire una funzione che prende 2 argomenti: un totale da pagare (float),
# e un intero come soldi consegnati al cassiere.
# la funzione deve calcolare il resto e generare una stringa che dica al
# cassiere quante e quali banconote o monete deve dare di resto. 
# la funzione può ritornare la stringa risultato oppure stamparla a video

def resto_contanti(importo, soldi):
    pass # cancellare questa riga e definire la funzione

## Es 2 
# definire una funzione che prende come argomento una frase o paragrafo (stringa)
# e una parola, quindi ritorna il numero di volte che la parola è contenuta nel 
# paragrafo

def conta_parola(paragrafo, parola):
    pass # cancellare questa riga e definire la funzione


## test della funzione - quando pensate di avere sritto bene la funzione, lanciate 
# il file e se la funzione è corretta il test viene superato

if conta_parola(
    """The interoffice memo at Electronic Musical Enterprise frightened Nat Flieger
      and he did not know why. It dealt, after all, with a great opportunity, the famed 
      Soviet pianist Richard Kongrosian, a psychokineticist who played Brahms and 
      Schumann without manually approaching the keyboard, had been located at his 
      summer home in Jenner, California. And, with luck, Kongrosian would be available 
      for a series of recording sessions with EME. And yet-Perhaps, 
      Flieger reflected, it was the dark, wet forests of the extreme northern coastal 
      region of California which repelled him; he liked the dry southlands near Tijuana, 
      here where EME maintained its central offices. But Kongrosian, according to the memo, 
      would not come out of his summer home; he had entered semi-retirement, possibly 
      due to some unknown domestic situation, hinted to be a tragedy involving either 
      his wife or his child. This had happened years ago, the memo implied.""",
      "the"      
      ) == 7:
    print("TEST SUPERATO\nCorretto! Ottimo lavoro")
else:
    print("TEST NON SUPERATO\nc'è qualcosa che non va... ricontrolla")

