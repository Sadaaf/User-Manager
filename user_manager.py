from tkinter import *
from tkinter import messagebox
from db import Parent
from db import Child

#Database Creation
db = Parent("user_data.db")
db1 = Child("user_data.db")
root=Tk()
root.title('User Manager')
root.geometry('1200x350')


#The Following Part Contains all the Necessary Methods and variables for the parent table
#Create a List generator for viewing the parents
def populate_list():
    user_data_list.delete(0, END)
    for row in db.fetch():
        user_data_list.insert(END, row)

#Create a method for adding items
def add_item():
    if fName_text.get() == '' or lName_text.get() == '' or street_text.get() == '' or city_text.get() == '' or state_text.get() == '' or zip_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(fName_text.get(), lName_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get())
    user_data_list.delete(0, END)
    user_data_list.insert(END, fName_text.get(), lName_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get())
    clear_text()
    populate_list()

#Selection Method
def select_item(event):
    try:
        global selected_item
        index = user_data_list.curselection()[0]
        selected_item = user_data_list.get(index)
        fName_entry.delete(0, END)
        fName_entry.insert(END, selected_item[1])
        lName_entry.delete(0, END)
        lName_entry.insert(END, selected_item[2])
        street_entry.delete(0, END)
        street_entry.insert(END, selected_item[3])
        city_entry.delete(0, END)
        city_entry.insert(END, selected_item[4])
        state_entry.delete(0, END)
        state_entry.insert(END, selected_item[5])
        zip_entry.delete(0, END)
        zip_entry.insert(END, selected_item[6])
    except IndexError:
        pass


#Delete method
def remove_item():
    db.remove(selected_item[0])
    db1.remove(selected_item[0])
    clear_child_text()
    populate_child_list()
    clear_text()
    populate_list()

#update the user info method
def update_item():
    if fName_text.get() == '' or lName_text.get() == '' or street_text.get() == '' or city_text.get() == '' or state_text.get() == '' or zip_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.update(fName_text.get(), lName_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get(), selected_item[0])
    populate_list()


#Clear the text fields
def clear_text():
    fName_entry.delete(0, END)
    lName_entry.delete(0, END)
    street_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)

# First Name
fName_text = StringVar()
fName_label = Label(root, text='First Name', font=('bold', 14), pady=20)
fName_label.grid(row=0, column=0, sticky=W)
fName_entry = Entry(root, textvariable=fName_text)
fName_entry.grid(row=0, column=1)
# Last Name
lName_text = StringVar()
lName_label = Label(root, text='Last Name', font=('bold', 14))
lName_label.grid(row=0, column=2, sticky=W)
lName_entry = Entry(root, textvariable=lName_text)
lName_entry.grid(row=0, column=3)
# Street
street_text = StringVar()
street_label = Label(root, text='Street', font=('bold', 14))
street_label.grid(row=1, column=0, sticky=W)
street_entry = Entry(root, textvariable=street_text)
street_entry.grid(row=1, column=1)
# City
city_text = StringVar()
city_label = Label(root, text='City', font=('bold', 14))
city_label.grid(row=1, column=2, sticky=W)
city_entry = Entry(root, textvariable=city_text)
city_entry.grid(row=1, column=3)
# State
state_text = StringVar()
state_label = Label(root, text='State', font=('bold', 14))
state_label.grid(row=2, column=0, sticky=W)
state_entry = Entry(root, textvariable=state_text)
state_entry.grid(row=2, column=1)
# Zip
zip_text = StringVar()
zip_label = Label(root, text='Zip Code', font=('bold', 14))
zip_label.grid(row=2, column=2, sticky=W)
zip_entry = Entry(root, textvariable=zip_text)
zip_entry.grid(row=2, column=3)

#Users List (Listbox)
user_data_list = Listbox(root, height=8, width=50, border=0)
user_data_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=7, column=3)
# Set scroll to listbox
user_data_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=user_data_list.yview)
# Bind select
user_data_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(root, text='Add New Parent', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(root, text='Remove Parent', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(root, text='Update Info', width=12, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(root, text='Clear Text Fields', width=12, command=clear_text)
clear_btn.grid(row=3, column=3)



#Separator
line1 = StringVar()
line1 =Label(root,text="---------------------").grid(row=0,column=4,columnspan=2)
line2 = StringVar()
line2 =Label(root,text="---------------------").grid(row=1,column=4,columnspan=2)
line3 = StringVar()
line3 =Label(root,text="---------------------").grid(row=2,column=4,columnspan=2)

#The Following Part Contains all the Necessary Methods and variables for the Child table

def populate_child_list():
    child_data_list.delete(0, END)
    for row in db1.fetch():
        print(row)
        child_data_list.insert(END, row)

def add_child_item():
    if fNameChild_text.get() == '' or lNameChild_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields in child info')
        return
    
    db1.insert(selected_item[0], fNameChild_text.get(), lNameChild_text.get()) #selected_item[0] is the primary key from Parent table to associate it with a parent
    child_data_list.delete(0, END)
    populate_child_list()

def select_child_item(event):
    try:
        global selected_child_item
        index1 = child_data_list.curselection()[0]
        selected_child_item = child_data_list.get(index1)
        fNameChild_entry.delete(0, END)
        fNameChild_entry.insert(END, selected_child_item[1])
        lNameChild_entry.delete(0, END)
        lNameChild_entry.insert(END, selected_child_item[2])
    except IndexError:
        pass
    
def remove_child_item():
    db1.remove(selected_child_item[0], fNameChild_entry.get(), lNameChild_entry.get())
    clear_child_text()
    populate_child_list()

def update_child_item():
    if fNameChild_text.get() == '' or lNameChild_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db1.update(fNameChild_text.get(), lNameChild_text.get(),selected_child_item[0])
    populate_child_list()

def clear_child_text():
    fNameChild_entry.delete(0, END)
    lNameChild_entry.delete(0, END)


# First Name
fNameChild_text = StringVar()
fNameChild_label = Label(root, text='Childs First Name', font=('bold', 14), pady=20)
fNameChild_label.grid(row=0, column=6, sticky=W)
fNameChild_entry = Entry(root, textvariable=fNameChild_text)
fNameChild_entry.grid(row=0, column=7)
# Last Name
lNameChild_text = StringVar()
lNameChild_label = Label(root, text='Childs Last Name', font=('bold', 14))
lNameChild_label.grid(row=1, column=6, sticky=W)
lNameChild_entry = Entry(root, textvariable=lNameChild_text)
lNameChild_entry.grid(row=1, column=7)

#Childs List (Listbox)
child_data_list = Listbox(root, height=8, width=50, border=0)
child_data_list.grid(row=4, column=5, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar for child list
scrollbar1 = Scrollbar(root)
scrollbar1.grid(row=7, column=8)
# Set scroll to listbox of child
child_data_list.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=child_data_list.yview)
# Bind select method to child list box
child_data_list.bind('<<ListboxSelect>>', select_child_item)

# Buttons
create_button = Button(root, text='Create New Child', width=14, command=add_child_item)
create_button.grid(row=3, column=6, pady=20)

delete_button = Button(root, text='Delete Child', width=14, command=remove_child_item)
delete_button.grid(row=3, column=7)

update_button = Button(root, text='Update Child Info', width=14, command=update_child_item)
update_button.grid(row=3, column=8)

clear_button = Button(root, text='Clear Text Fields', width=14, command=clear_child_text)
clear_button.grid(row=3, column=9)

# Populate data in child list
populate_child_list()
# Populate data in parent list
populate_list()





root.mainloop()