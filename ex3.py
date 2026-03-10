hex_num = input()
oct_num = input()

a = int(hex_num, 16)
b = int(oct_num, 8)

print(max(a, b))