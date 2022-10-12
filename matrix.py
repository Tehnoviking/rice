matrix=[
    [2,3,4,5],
    [6,3,2,5],
    [7,8,4,2]
]
#Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Найти сумму элементов всей матрицы. Определить, какую долю в этой сумме составляет сумма элементов каждого столбца.
# Результат оформить в виде матрицы из N+1 строк и M столбцов.
summa=0
for element_str in range(3):
    for element_stl in range(4):
        summa+=matrix[element_str][element_stl]
    print(summa)

summa_all=0
for element_str in matrix:
    for element_stl in element_str:
        summa_all+=element_stl
print(summa_all)

#Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Перемножить элементы каждого столбца матрицы с соответствующими элементами К­го столбца.
k=2
b=[]
for j in range(4):
    for i in range(3):
        b.append(matrix[i][j]*matrix[i][k])
print(b)

#Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Просуммировать элементы каждой строки матрицы с соответствующими элементами L ­ той строки.
k=1
b=[]
for i in range(3):
    for j in range(4):
        b.append(matrix[i][j]*matrix[k][j])
print(b)





