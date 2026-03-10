a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Czy pierwsza jest większa od drugiej:", a > b)
print("Czy liczby są równe:", a == b)
print("Czy pierwsza jest parzysta ORAZ druga nieparzysta:", a % 2 == 0 and b % 2 != 0)
print("Czy którakolwiek liczba jest większa niż 100:", a > 100 or b > 100)