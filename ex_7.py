a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

largest = max(a, b, c)
smallest = min(a, b, c)

difference = abs(largest - smallest)

print("Największa liczba:", largest)
print("Najmniejsza liczba:", smallest)
print("Różnica bezwzględna:", difference)