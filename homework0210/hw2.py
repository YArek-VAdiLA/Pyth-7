days = int(input("Введите количество дней: "))
discaunt = int(input("Введите процент скидки: "))
price = int(input("Введите сумму: "))

thisDay = 1
sumPrice = 0
# while thisDay <= days:
#     finalPrice = price - ((discaunt / 100) * price)
#     sumPrice = finalPrice + sumPrice
#     print(thisDay)
#     thisDay += 1        # thisDay = thisDay + 1, thisDay++
#     price += 3

for day in range(days):
    finalPrice = price - ((discaunt / 100) * price)
    sumPrice = finalPrice + sumPrice
    price += 3

print("Прибыль за", days, "дней:", sumPrice)