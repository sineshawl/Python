from customtkinter import *
from tkinter import ttk

# Create the main application window
window = CTk()
window.title("Treeview Example")

# Create a frame to hold the Treeview widget
frame = CTkFrame(window)
frame.pack(fill=BOTH, expand=True)

# Create a Treeview widget inside the frame
cols = ([i for i in range(13)])

tree = ttk.Treeview(frame, show='headings', columns=cols)
tree.pack(side=LEFT, fill=BOTH, expand=True)

# # Configure the columns

for colname in cols:
    tree.column(colname, anchor=CENTER, width=40)
    tree.heading(colname, text=colname)

values=[i for i in range(13)]
keys=['A','B','C','D','E','F','H']
my_dict ={}
for key in keys:
    my_list = []
    for value in values:
        if value == 0:
            my_list.append(key)
        else:
            my_list.append(key+str(value))
    my_dict[key] = my_list


print(my_dict['A'])

# Configure the headings
# tree.column('#0', anchor=CENTER, width=80)
# tree.heading("#0", text="", anchor=CENTER)

# for i in range(12):
#     tree.column(i+1, anchor=CENTER, width=80)
#     tree.heading(i+1, text=i+1, anchor=CENTER)

# # Add some items to the Treeview
for key in my_dict.keys():
    tree.insert(parent="", index="end", id=key, text="", values=tuple(my_dict[key]))


# # Add a vertical scrollbar to the Treeview
# scrollbar = CTkScrollbar(frame, orientation=VERTICAL, command=tree.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# tree.configure(yscrollcommand=scrollbar.set)

window.mainloop()
