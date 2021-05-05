# GUI to calorie_calculator

from tkinter import *
import pandas as pd

# Products database
df = pd.read_csv("calorie_base.csv")

# Counter for adequate row
counter = 0

# Window object
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

l8 = Label(window, text="Delete buttons", padx=20, pady=20)
l8.grid(row=0, column=6)

# Add product by pressing "add button"
def add_product_from_list():
    global counter
    counter += 1
    add_listed_product = name_entry.get()

    weight_entry = Entry(window, width=15)
    weight_entry.grid(row=counter, column=5)

    l1 = Label(window, text=df.loc[df['Name']==add_listed_product,'Name'].item(), padx=20, pady=5)
    l1.grid(row=counter, column=0)

    l2 = Label(window, text=df.loc[df['Name']==add_listed_product,'Carbs'].item(), padx=20, pady=5)
    l2.grid(row=counter, column=1)

    l3 = Label(window, text=df.loc[df['Name']==add_listed_product,'Protein'].item(), padx=20, pady=5)
    l3.grid(row=counter, column=2)

    l4 = Label(window, text=df.loc[df['Name']==add_listed_product,'Fat'].item(), padx=20, pady=5)
    l4.grid(row=counter, column=3)

    l5 = Label(window, text=df.loc[df['Name']==add_listed_product,'Calories'].item(), padx=20, pady=5)
    l5.grid(row=counter, column=4)

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
    name_entry.insert(0, product_list.get(ACTIVE))          #Add clicked list item to entry box

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

# Define buttons
add_product = Button(window, text="Add product", padx=20, pady=20, command=add_product_from_list)
add_product.grid(row=0, column=7)

# Update function call
update(df['Name'])

# Create a binding on the listbox onclick
product_list.bind("<<ListboxSelect>>", fillout)

#Create a binding on the entry box
name_entry.bind("<KeyRelease>", check)

window.mainloop()
