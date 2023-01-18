tickets = int(input("Сколько билетов,  вы хотите приобрести: "))
cost_total = 0

for i in range(tickets):
    age = int(input(f"Введите возраст посетителя {i+1} "))
    if age < 18:
        cost = 0
    elif 25 > age >= 18:
        cost = 990
    else:
        cost = 1390
    print("Стоимость  этого билета составит: ", cost)
    cost_total += cost
    print('*'*33)

if tickets > 3:
    cost_total -= (cost_total * .1)

print("")
print("Всего к оплате, с учётом всех возможных скидок: ", cost_total, 'руб.')