"""
Stringhe dal livello zero al livello supereroe!

tipi di stringa:
 - in linea: testo contornato da vigolette ("") o apici ('') 
 - multilina: 3 virgolette come questo commento

Stringa vuota: "" oppure ''

"""

"""
1) composizione di stringhe
Ci sono vari modi per comporre una stringa:
 - operatore + 
 - formattare una stringa (con f"" oppure il metodo .format() vedi https://www.w3schools.com/python/ref_string_format.asp) 

"""
h_w = "hello world!"
saluto = "hello"
nome = "Joe"

frase_finale = h_w + '\n' + saluto + ' ' + nome # inserisco spazi e carattere a capo come stringhe costanti

print(frase_finale)

frase_finale_formattata = f"{h_w}\n{saluto} {nome}"

print(frase_finale_formattata)

frase_finale_f = "{0}\n{2} {1}".format(h_w, nome, saluto) # i numeri nelle graffe della stringa sono gli indici degli elementi passati dentro a format()
print(frase_finale_f)