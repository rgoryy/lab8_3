import tkinter as tk
from tkinter import *
import random
import matplotlib.pyplot as plt

window = tk.Tk()

# Создаем массив для вероятностей
probabilities = [0.15, 0.25, 0.1, 0.2]
# Добавляем последнюю вероятность как сумму всех предыдущих
probabilities.append(1 - sum(probabilities))

label_p1 = Label(text="Prob. 1:")
label_p1.pack()
entry_p1 = Entry()
entry_p1.insert(0, "0.15")
entry_p1.pack()

label_p2 = Label(text="Prob. 2:")
label_p2.pack()
entry_p2 = Entry()
entry_p2.insert(0, "0.25")
entry_p2.pack()

label_p3 = Label(text="Prob. 3:")
label_p3.pack()
entry_p3 = Entry()
entry_p3.insert(0, "0.1")
entry_p3.pack()

label_p4 = Label(text="Prob. 4:")
label_p4.pack()
entry_p4 = Entry()
entry_p4.insert(0, "0.2")
entry_p4.pack()

label_res_p5 = Label(text="Prob. 5")
label_res_p5.pack()

entry_p5 = Entry()
entry_p5.insert(0, "")
entry_p5.pack()

label_trials = Label(text="Trials")
label_trials.pack()

num_trials_var = tk.StringVar(window)
num_trials_var.set("10")
num_trials_options = ["10", "100", "1000", "10000"]

entry_trials = OptionMenu(window, num_trials_var, *num_trials_options)

entry_trials.pack()

def button_clicked():
    # Обновляем вероятности из полей ввода
    probabilities[0] = float(entry_p1.get())
    probabilities[1] = float(entry_p2.get())
    probabilities[2] = float(entry_p3.get())
    probabilities[3] = float(entry_p4.get())
    probabilities[4] = 1 - sum(probabilities)  # Обновляем последнюю вероятность

    num_trials = int(num_trials_var.get())
    values = []

    for _ in range(num_trials):
        rand_value = random.random()
        comp_value = 0
        number = 0
        for prob in probabilities:
            number += 1
            comp_value += prob
            if rand_value < comp_value:
                values.append(number)
                break

    plt.clf()
    plt.hist(values, bins=range(1, 7), edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.title('Histogram of Values')
    plt.show()
    print(values)

button = tk.Button(window,
                   text="Build Histogram",
                   command=button_clicked,
                   font=("Arial", 14))
button.pack()

window.mainloop()