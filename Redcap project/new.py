import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("column1", "column2"), show="headings")
tree.heading("#1", text="Column 1")
tree.heading("#2", text="Column 2")

# Insert sample data
for i in range(10):
    tree.insert("", "end", values=("Value " + str(i), "Value " + str(i)))

# Configure background color for specific columns
tree.tag_configure("column1_tag", background="lightblue")
tree.tag_configure("column2_tag", background="lightgreen")

# Tag all cells in the first column with "column1_tag"
for i in range(10):
    tree.tag_configure("cell_tag_" + str(i), background="lightblue")
    tree.item(tree.get_children()[i], tags=("cell_tag_" + str(i),))

# Tag all cells in the second column with "column2_tag"
# for i in range(10):
#     tree.tag_configure("cell_tag_" + str(i), background="lightgreen")
#     tree.item(tree.get_children()[i], tags=("cell_tag_" + str(i),))

# Pack the Treeview widget
tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()
