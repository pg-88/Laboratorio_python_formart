s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(s.split()))

lista_parole = s.split() # split ritorna una lista!!!!
print(lista_parole, len(lista_parole))

dolor_presente = 0

for parola in lista_parole: 
    if parola == 'dolor':
        dolor_presente += 1 # incremento e riassegno il valore 
        # esempio i += 1 equivale a i = i + 1
        print(dolor_presente)
print(f"nella stringa {s} la parola 'dolor' compare {dolor_presente} volte")



stringa_under = "qui_non_ci_sono_spazi_ma_voglio_comunque_separare_con_split"

splitted_under = stringa_under.split('_')
print(splitted_under)