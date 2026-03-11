# Zadanie 20: Mix typów złożonych

# Utworzenie słownika z informacjami o filmie
film = {
    "tytuł": "Inception",
    "rok": 2010,
    "gatunki": ["akcja", "sci-fi", "thriller"],
    "oceny": (8, 9, 7)
}

# Wyświetlenie wszystkich informacji o filmie
print("Informacje o filmie:", film)

# Wyświetlenie pierwszego gatunku z listy
print("Pierwszy gatunek:", film["gatunki"][0])

# Obliczenie i wyświetlenie średniej ocen
srednia_ocen = sum(film["oceny"]) / len(film["oceny"])
print("Średnia ocen:", srednia_ocen)
