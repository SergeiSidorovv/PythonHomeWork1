# Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
#  если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

count_crane = int(input("Введите количество журавликов сделанных детьми: "))

cranes_made_by_Sergey_or_Peter = (count_crane // 3) // 2

cranes_made_by_Kate = (count_crane // 3) * 2

print(f"количество журавликов сделанное Сергеем - {cranes_made_by_Sergey_or_Peter}")
print(f"количество журавликов сделанное Катей - {cranes_made_by_Kate}")
print(f"количество журавликов сделанное Петей - {cranes_made_by_Sergey_or_Peter}")
