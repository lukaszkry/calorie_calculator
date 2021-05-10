# GUI to calorie_calculator

from tkinter import *
import pandas as pd
import os

# Products database
df = pd.read_csv("calorie_base.csv")

# Global variables
counter = 2             # Counter for adequate row
weight = 0
carbs = 0
proteins = 0
fats = 0
calories = 0

# Main window object
window = Tk()

# Define entries
name_entry = Entry(window, width=40)
name_entry.grid(row=1, column=7)

# Define listbox
product_list = Listbox(window, width=50)
product_list.grid(row=2, column=7)

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

l6 = Label(window, text="Sum", padx=20, pady=20)
l6.grid(row=99, column=0)

l7 = Label(window, text="Amount (grams)", padx=20, pady=20)
l7.grid(row=0, column=5)


# Add product by pressing "add button"
def add_product_from_list():
    global counter, carbs, proteins, fats, calories
    counter += 1
    add_listed_product = name_entry.get()

    carb = round(df.loc[df['Name'] == add_listed_product, 'Carbs'].item()*weight/100, 3)
    protein = round(df.loc[df['Name'] == add_listed_product, 'Protein'].item()*weight/100, 3)
    fat = round(df.loc[df['Name'] == add_listed_product, 'Fat'].item()*weight/100, 3)
    kcal = round(df.loc[df['Name'] == add_listed_product, 'Calories'].item()*weight/100, 3)

    carbs = round(carbs + carb, 3)
    proteins = round(proteins + protein, 3)
    fats = round(fats + fat, 3)
    calories = round(calories + kcal, 3)

    label1 = Label(window, text=df.loc[df['Name'] == add_listed_product, 'Name'].item(), padx=20, pady=5)
    label1.grid(row=counter, column=0)

    label2 = Label(window, text=carb, padx=20, pady=5)
    label2.grid(row=counter, column=1)

    label3 = Label(window, text=protein, padx=20, pady=5)
    label3.grid(row=counter, column=2)

    label4 = Label(window, text=fat, padx=20, pady=5)
    label4.grid(row=counter, column=3)

    label5 = Label(window, text=kcal, padx=20, pady=5)
    label5.grid(row=counter, column=4)

    label6 = Label(window, text=weight, padx=20, pady=5)
    label6.grid(row=counter, column=5)

    l8 = Label(window, text=carbs, padx=20, pady=20)
    l8.grid(row=99, column=1)

    l9 = Label(window, text=proteins, padx=20, pady=20)
    l9.grid(row=99, column=2)

    l10 = Label(window, text=fats, padx=20, pady=20)
    l10.grid(row=99, column=3)

    l11 = Label(window, text=calories, padx=20, pady=20)
    l11.grid(row=99, column=4)

    print(df.loc[df['Name'] == add_listed_product])
    print(counter)


# Update the listbox
def update(data):
    product_list.delete(0, END)                 # Clear the listbox
    for product in data:
        product_list.insert(END, product)


# Update entry box with listbox clicked
def fillout(event):
    name_entry.delete(0, END)                   # Clear entry box
    name_entry.insert(0, product_list.get(ACTIVE))          # Add clicked list item to entry box


# Create function to check whether product is on the list
def check(event):
    typed = name_entry.get()      # Grab what was typed
    if typed == '':
        data = df['Name']
    else:
        data = []
        for item in df['Name']:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)        # Update listbox with selected product


# Product mass input window
def mass():

    def complete_product():
        global weight
        weight = int(mass_entry.get())
        top.destroy()
        add_product_from_list()

    top = Toplevel()
    top.title('Type product mass')
    mass_entry = Entry(top, width=25)
    mass_entry.pack()
    add_button = Button(top, text='ADD', padx=10, pady=10, command=complete_product)
    add_button.pack()


# Reset calculator function
def restart():
    window.destroy()
    os.startfile("GUI.py")


# Define buttons
add_product = Button(window, text="Add product", padx=20, pady=20, command=mass)
add_product.grid(row=0, column=7)

reset_button = Button(window, text="RESET", padx=20, pady=20, command=restart)
reset_button.grid(row=0, column=8)

# Update function call
update(df['Name'])

# Create a binding on the listbox onclick
product_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
name_entry.bind("<KeyRelease>", check)

window.mainloop()
