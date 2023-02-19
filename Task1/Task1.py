# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number  = int(input("Введите трёхзначное число: "))

first_figure_in_number = ((number // 10) // 10)

second_figure_in_number = (number // 10) % 10

third_figure_in_number = number % 10

print(f"Сумма цифр трёхзначного числа = {first_figure_in_number + second_figure_in_number + third_figure_in_number}")
