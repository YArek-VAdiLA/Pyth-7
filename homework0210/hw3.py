katet1 = int(input("Введите катет: "))
katet2 = int(input("Введите катет: "))

gip = ((katet1 ** 2) + (katet2 ** 2)) ** 0.5
print("Гипотенуза: ", gip)

print("Периметр: ", katet1 + katet2 + gip)

print("Площадь: ", 0.5 * katet1 * katet2)