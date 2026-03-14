dni_tygodnia = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek")

print("Cała krotka:", dni_tygodnia)
print("Drugi dzień:", dni_tygodnia[1])
print("Długość krotki:", len(dni_tygodnia))
try:
    dni_tygodnia[0] = "niedziela"
except TypeError as e:
    print("Błąd podczas próby zmiany elementu krotki:", e)
