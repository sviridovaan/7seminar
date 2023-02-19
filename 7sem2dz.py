#Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов 
# идет с единицы (подумайте, почему не с нуля).
# При нумерации с нуля результирующей таблицей будет заполненная 
# нулями первая строка и первый столбец

def print_operation_table(operation, num_rows=6, num_columns=6) :
    for i in range(1, num_rows + 1) :
        list_1 = []    
        for j in range(1, num_columns + 1):
            list_1.append(operation(i, j))
        print(*list_1)


print_operation_table(lambda x, y : x * y)
