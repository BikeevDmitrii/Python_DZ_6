# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_1 = [1, 3, 4, 6, 10, 11, 15, 12, 14]
list_2 = list(filter(lambda x: (x%2 != 0) , list_1))
print(list_2)
print(sum(list_2))
