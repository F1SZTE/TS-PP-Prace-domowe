zdanie = input("Podaj zdanie: ")
litera = input("Podaj literę: ")
liczba_wystapien = zdanie.lower().count(litera.lower())
print(f"Litera '{litera}' występuje {liczba_wystapien} razy w zdaniu.")
