g = 9.80665

a = float(input())
t = float(input())

print("*" * 80)

print(a > g)

s = 0.5 * a * t ** 2
print(round(s, 2))

a_g = a / g
a_g_rounded = round(a_g * 2) / 2
print(a_g_rounded)

print(2 <= a_g_rounded <= 4)