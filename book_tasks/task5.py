'''
Упражнение 5. Сдаем бутылки

(Решено. 15 строк)
Во многих странах в стоимость стеклотары закладывается определенный

депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
ки большего объема – $0,25.

Напишите программу, запрашивающую у пользователя количество бу-
тылок каждого размера. На экране должна отобразиться сумма, которую
можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
вывод так, чтобы сумма включала два знака после запятой и дополнялась
слева символом доллара.
'''

bottle_less_one_litre = int(input("Enter quantity bottle less one liter: "))
bottle_more_one_litre = int(input("Enter quantity bottle more one liter: "))

price_less_one_litre = 0.1
price_more_one_litre = 0.25

revenue  = bottle_less_one_litre * price_less_one_litre + bottle_more_one_litre * price_more_one_litre

print("\nQuantity bottle less one liter: " + str(bottle_less_one_litre))
print("Price one bottle less one liter: " + str(price_less_one_litre) + "$")

print("Quantity bottle more one liter: " + str(bottle_more_one_litre))
print("Price one bottle more one liter: " + str(price_more_one_litre) + "$")

print("Total revenue: " + str(revenue) + "$")



