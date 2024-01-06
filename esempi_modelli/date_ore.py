import datetime
# Libreria per gestire il tempo le date e le durate di tempo

"""
Permette sia di eseguire operazione con date e tempo sia di estrarre dati
di tipo datetime (timestamp, accesso, lettura, creazione dei file)
e di rappresentarli con un output formattato
"""

# creo (istanzio) un oggetto datetime

ora = datetime.datetime(1955, 11, 12, 6, 38)
print("oggetto datetime", ora, "\ndel tipo:", type(ora))

adesso = datetime.datetime.now()
print("adesso: ", adesso)
print("in che anno siamo:", adesso.year)
print("Data", adesso.date())
# formattare date e orari https://docs.python.org/3.10/library/datetime.html#strftime-and-strptime-format-codes
print("Data gg/mm/aaaa", adesso.strftime("%d/%m/%Y ora: %H:%M:%S"))

# aggiungere un'ora:
incremento = datetime.timedelta(hours=1)

fine = adesso + incremento * 8 
print("la giornata lavorativa finisce alle: ", fine)
print(f"Oggi {adesso.strftime('%A %d, %B')}si lavora!")

print("Inizio turno", datetime.datetime(2024, 1, 8, 9, 0), " fine turno ", datetime.time(17,0))

# prossimo compleanno
compleanno = datetime.date(year=2024, month=1, day=2)
# condizione con le date:
if datetime.date.today() == compleanno:
    print("buon compleanno")
elif datetime.date.today() < compleanno:
    print("il tuo compleanno sarà tra ", compleanno - datetime.date.today())
elif datetime.date.today() > compleanno:
    print("il compleanno è passato da ", datetime.date.today() - compleanno)
