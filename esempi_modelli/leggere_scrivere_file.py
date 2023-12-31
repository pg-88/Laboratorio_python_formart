'''
Per lavorare con i file in python possiamo usare la funzione built-in open
'''

file_nuovo = open("risorse/file_generato.txt", 'w')
# apre un file che sta nella cartella risorse e si chiama file generato
# se il file non esiste viene generato e aperto per scrittura
# il secondo argomento è la modalità di apertura w sta per scrittura (write)

file_nuovo.write("Hello World!")
# scrive una stringa nel file 
file_nuovo.close()
# controlla la cartella e ci sarà un file di testo 
# (ammesso che lanci lo script dalla cartella /nuovo_progetto_python_formart)

'''################### file nelle funzioni ###############################'''

def leggi_file(nome_file):
    ''' Apre il file (se esiste) e fa il print del contenuto 
    se il file non esiste stampa un errore

    :param nome_file: percorso del file nel sistema 
    '''
    f = open(nome_file, 'r')
    print("contenuto file:\n", f.read())
    f.close()

## chiamata della funzione con nome a caso -> da errore
# leggi_file("Ajeye Brazorf")  # commentare questa riga se vuoi eseguire il resto dello script

# gestione errore 
try:
    leggi_file("test")
except FileNotFoundError as err:
    print("Il file non esiste, creiamolo:\n")
    file_creato = open("test", 'w')
    file_creato.close()
    leggi_file("test")

'''N.B. Per evitare problemi nella scrittura e la possibilità che i file vengano 
corrotti, bisongna SEMPRE chiudere il file con il metodo close. 
Si può usare lo statement with che gestisce l'apertura e la chiusura dello stream del file
Esempio: '''

with open("risorse/file_generato.txt", 'r') as file_txt:
    print("contenuto file:\n", file_txt.read())

# qui la variabile file_txt non esiste più 
try:
    print("il file contiene", file_txt.read())
except: 
    print("siamo fuori dallo scope del with quindi la variabile non esiste più")


'''
Usare il with nelle funzioni
'''
def scrive_legge_file(nome_file, contenuto_da_aggiungere):
    '''apre file per aggiungere la stringa con il flag 'a' per append
    scrive la stringa del contenuto_da_aggiungere'''
    with open(nome_file, 'a') as file_aperto:
        file_aperto.write(contenuto_da_aggiungere)

    # print del contenuto del file
    with open(nome_file, 'r') as leggere_file:
        print("Contenuto File:", leggere_file.read())

scrive_legge_file("risorse/file_generato.txt", "Lorem Ipsum")
