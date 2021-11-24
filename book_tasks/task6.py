"""
Упражнение 6. Налоги и чаевые

(Решено. 17 строк)

Программа, которую вы напишете, должна начинаться с запроса у поль-
зователя суммы заказа в ресторане. После этого должен быть произведен
расчет налога и чаевых официанту. Вы можете использовать принятую
в вашем регионе налоговую ставку для подсчета суммы сборов.

 В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
де программа должна отобразить отдельно налог, сумму чаевых и итог,

включая обе составляющие. Форматируйте вывод таким образом, чтобы
все числа отображались с двумя знаками после запятой.
"""

amount_order = int(input("Enter amount of you order: "))
tax_nds = (amount_order/100) * 20
gratuity = (amount_order/100) * 18
result = amount_order + gratuity

#print("%.2f" % x)
#print("%s съел %d пирожков!" % (name, numCookies))


print("\n Tax nds: "+"%.2f" % tax_nds)
print("Gratuity for waiter: " + str(gratuity))
print("Result: " + str(result))

str_res =  "Tax nds str_res: "+"%.7f" % tax_nds

print(str_res)
print(type(str_res))

tax_nds_str = "%.2s" % tax_nds
print(type(tax_nds_str))
print(type(tax_nds))

