liczba = int(input("Podaj liczbę dziesiętną: "))

print("System szesnastkowy:", hex(liczba)[2:])
print("System ósemkowy:", oct(liczba)[2:])

# [2:] usuwa prefiks 0x i 0o dodany przez finkcje hex i oct (tak samo jak przez bin)