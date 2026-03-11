# Zadanie 17: Krotki (tuple)

# Utworzenie krotki z dniami tygodnia
dni_tygodnia = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek")

# Wyświetlenie całej krotki
print("Cała krotka:", dni_tygodnia)

# Wyświetlenie drugiego dnia
print("Drugi dzień:", dni_tygodnia[1])

# Wyświetlenie długości krotki
print("Długość krotki:", len(dni_tygodnia))

# Próba zmiany pierwszego elementu krotki
try:
    dni_tygodnia[0] = "niedziela"
except TypeError as e:
    print("Błąd podczas próby zmiany elementu krotki:", e)
