# Напишите программу, которая выводит попарно элементы 2 списков

list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 8]
for x, y in zip(list_2, list_1):
	print(y, x)
