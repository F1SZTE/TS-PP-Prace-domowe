import math

liczba = float(input("Podaj liczbę: "))

wartosc_bezwzgledna = abs(liczba)
potega = liczba ** 3
pierwiastek = math.sqrt(wartosc_bezwzgledna)

print("Wartość bezwzględna:", wartosc_bezwzgledna)
print("Liczba do potęgi 3:", potega)
print("Pierwiastek z wartości bezwzględnej:", pierwiastek)