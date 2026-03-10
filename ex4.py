text = input()

print(len(text))
print(text.lower().count('t'))
print(text.startswith("TechniSchools"))

try:
    float(text)
    print(True)
except:
    print(False)