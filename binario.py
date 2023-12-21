numero = 42

potenze_due = [2 ** i for i in range(0, 10)]
print(potenze_due)

print(numero % 10)
unita = numero % 10 
print(unita, unita // 2, unita % 2)

numero_loop = numero # variabile di appoggio per preservare la variabile numero
stringa_num_bin = "" # conterrà il risultato

while numero_loop >= 1:
    stringa_num_bin = str(numero_loop % 2) + stringa_num_bin
    numero_loop = numero_loop // 2
    print("stringa", stringa_num_bin,"numero residuo", numero_loop)
print("output", stringa_num_bin)
