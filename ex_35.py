magazyn = {"jabłka": 50, "banany": 30, "pomarańcze": 25}

owoc = input("Podaj nazwę owocu: ")

if owoc in magazyn:
    print(magazyn[owoc])
else:
    print("Brak w magazynie")