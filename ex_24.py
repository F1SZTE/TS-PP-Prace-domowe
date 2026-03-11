# Zadanie 24: Liczenie wystąpień

# Zapytanie użytkownika o zdanie
zdanie = input("Podaj zdanie: ")

# Zapytanie użytkownika o literę
litera = input("Podaj literę: ")

# Liczenie wystąpień litery w zdaniu (bez uwzględniania wielkości liter)
liczba_wystapien = zdanie.lower().count(litera.lower())

# Wyświetlenie wyniku
print(f"Litera '{litera}' występuje {liczba_wystapien} razy w zdaniu.")
