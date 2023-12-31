import tkinter as tk

#  тут добавляю символы (цифры) в поле ввода
def добавить_ввод(значение):
    текущее_выражение = поле_ввода.get()
    новое_выражение = текущее_выражение + str(значение)
    поле_ввода.delete(0, tk.END)  # Очистка
    поле_ввода.insert(0, новое_выражение)

# вычисления результата и вывод его в поле ввода
def вычислить():
    try:
        выражение = поле_ввода.get()
        результат = eval(выражение)
        поле_ввода.delete(0, tk.END)  # Очистка
        поле_ввода.insert(0, результат)
    except:
        поле_ввода.delete(0, tk.END)  # Очистка
        поле_ввода.insert(0, "Ошибка")

# Функция для очистки
def очистить_ввод():
    поле_ввода.delete(0, tk.END)

# Создание основного окна
окно = tk.Tk()
окно.title("Калькулятор")

# поле для ввода
поле_ввода = tk.Entry(окно, font=("Arial", 20))
поле_ввода.grid(row=0, column=0, columnspan=4)

# Список кнопок
кнопки = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

# Создание кнопок и их размещение
строка, столбец = 1, 0
for текст_кнопки in кнопки:
    кнопка = tk.Button(окно, text=текст_кнопки, padx=20, pady=20, font=("Arial", 16))
    кнопка.grid(row=строка, column=столбец)
    столбец += 1
    if столбец > 3:
        столбец = 0
        строка += 1

    # Назначение функций для кнопок
    if текст_кнопки.isdigit() or текст_кнопки in "+-*/.":
        кнопка.configure(command=lambda значение=текст_кнопки: добавить_ввод(значение))
    elif текст_кнопки == '=':
        кнопка.configure(command=вычислить)
    elif текст_кнопки == 'C':
        кнопка.configure(command=очистить_ввод)

окно.mainloop()
