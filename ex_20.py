film = {
    "tytuł": "Inception",
    "rok": 2010,
    "gatunki": ["akcja", "sci-fi", "thriller"],
    "oceny": (8, 9, 7)
}

print("Informacje o filmie:", film)
print("Pierwszy gatunek:", film["gatunki"][0])
srednia_ocen = sum(film["oceny"]) / len(film["oceny"])
print("Średnia ocen:", srednia_ocen)
