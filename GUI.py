# GUI to calorie_calculator

from tkinter import *
import pandas as pd

# Products database
df = pd.read_csv("calorie_base.csv")

# Window object
window = Tk()

# Define entries
name_entry = Entry(window, width=40)
name_entry.grid(row=1, column=5)

# Define labels
l1 = Label(window, text="Product", padx=20, pady=20)
l1.grid(row=0, column=0)

l2 = Label(window, text="Carbs", padx=20, pady=20)
l2.grid(row=0, column=1)

l3 = Label(window, text="Proteins", padx=20, pady=20)
l3.grid(row=0, column=2)

l4 = Label(window, text="Fats", padx=20, pady=20)
l4.grid(row=0, column=3)

l5 = Label(window, text="Calories", padx=20, pady=20)
l5.grid(row=0, column=4)

l6 = Label(window, text="Sum")
l6.grid(row=99, column=0)

def add_product_from_list():
    add_listed_product = name_entry.get()
    print(df.loc[df['Name'] == add_listed_product])

# Define buttons
add_product = Button(window, text="Add product", padx=20, pady=20, command=add_product_from_list)
add_product.grid(row=0, column=5)

window.mainloop()
