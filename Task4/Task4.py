# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите кол-во долек шоколадки по ширине: "))
m = int(input("Введите кол-во долек шоколадки по длинне: "))

count_slices = int(input("Введите кол-во долек которое вы хотите отломить: "))

size_chocolate = n * m

if count_slices <= size_chocolate // 2:
    print("У вас получится отломить столько долек")
else:
    print("Ищите другую шоколадку")
