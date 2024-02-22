import customtkinter
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from customtkinter import CTk
from project_setting import projectSetting



class leftFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=15)
        self.columnconfigure(0, weight=1)
        
        self.inner_frame1 = ctk.CTkFrame(self, fg_color="gray", corner_radius=100 , width=100, height=100)
        self.inner_frame1.grid(row = 0, column=0,padx=5)


        self.inner_frame2 = ctk.CTkFrame(self, fg_color="gray", corner_radius=10)
        self.inner_frame2.grid(row = 1, column=0, padx=10, pady=(10, 30), sticky="nsew")
    
        self.inner_frame2.columnconfigure(0, weight=1)

        self.label_user = ctk.CTkLabel(self.inner_frame2, text="user", font=('Arial', 20), )
        self.label_user.grid(row = 0, column=0, padx=10, pady=2, sticky='ew')
        

        self.btn = ctk.CTkButton(self.inner_frame2, text='project setting', font=('Arial', 10),command=lambda: projectSetting(master))
        self.btn.grid(row = 1, column=0, padx=2, pady=(30, 0), sticky='ew')

        for i in range(3):
            self.button = ctk.CTkButton(self.inner_frame2, text=f'Button {i+1}', font=('Arial', 15))
            self.button.grid(row = i+2, column=0, padx=2, pady=2, sticky='nsew')


        self.switch_themer =ctk.CTkSwitch(self.inner_frame2, text="switch Theme", command=lambda : self.switch_theme(), onvalue="on", offvalue="of")
        self.switch_themer.grid(row = 5, column=0, padx=10, pady=10, sticky='nsew')


  



    def switch_theme(self):
        if self._get_appearance_mode() == 'dark':
            customtkinter.set_appearance_mode('light')
            style = ttk.Style()
            # Customize the Treeview widget style
            style.configure("Treeview", background="#EBEBEB", fieldbackground="#EBEBEB", foreground="black", borderwidth=10 )

        else:
            customtkinter.set_appearance_mode('dark')
            style = ttk.Style()
            # Customize the Treeview widget style
            style.configure("Treeview", background="#646668", fieldbackground="#646668", foreground="white")



        

class middleFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=5)
        self.rowconfigure(tuple(range(12)), weight=1)
  
        
        self.inner_frame1 = ctk.CTkFrame(self, fg_color="gray", corner_radius=10, height=120 )
        self.inner_frame1.grid(row = 0, column=0, padx=10, pady=(10,0), sticky="ew")

        self.inner_frame2 = ctk.CTkFrame(self, fg_color="gray", corner_radius=10)
        self.inner_frame2.grid(row = 1, rowspan=11, column=0, padx=10, pady=(2,30), sticky="nsew")


        self.inner_frame2.rowconfigure(tuple(range(9)), weight=1)
        self.inner_frame2.columnconfigure(tuple(range(12)), weight=1)

        self.option = ctk.CTkOptionMenu(self.inner_frame2,values=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5'])
        self.option.grid(row=9, column=0, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {1}', text_color= ('black', 'white'), fg_color='transparent', command= self.tab_viewer(1))
        self.btn_tabviewer.grid(row=9, column=1, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {2}', fg_color='transparent', command=lambda: self.tab_viewer(2))
        self.btn_tabviewer.grid(row=9, column=2, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {3}', fg_color='transparent', command=lambda: self.tab_viewer(3))
        self.btn_tabviewer.grid(row=9, column=3, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {4}', fg_color='transparent', command=lambda: self.tab_viewer(4))
        self.btn_tabviewer.grid(row=9, column=4, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {5}', fg_color='transparent', command=lambda: self.tab_viewer(5))
        self.btn_tabviewer.grid(row=9, column=5, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab {6}', fg_color='transparent', command=lambda: self.tab_viewer(5))
        self.btn_tabviewer.grid(row=9, column=6, padx=2, pady=2, sticky='ew')

        self.btn_tabviewer = ctk.CTkButton(self.inner_frame2, text=f'Tab 7', fg_color='transparent', command=lambda: self.tab_viewer(5))
        self.btn_tabviewer.grid(row=9, column=7, padx=2, pady=2, sticky='ew')


        # self.tab_view1 = ctk.CTkTabview(self.inner_frame2)
        # self.tab_view1.grid(row=0, rowspan=9, column =0, padx=2, pady=2, columnspan=13, sticky='nsew')

        # self.label = ctk.CTkLabel(self.tab_view1, text=f'Tab 1')
        # self.label.place(relx=0.5, rely=0.5)
  


    def tab_viewer(self, i):

        # color = ['red', 'green', 'yellow', 'blue', 'cyan']
        # self.tab_view1 = ctk.CTkTabview(self.inner_frame2)
        # self.tab_view1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.90)

        # self.tab_view1.grid(row=0, rowspan=9, column =0, padx=2, pady=2, columnspan=13, sticky='nsew')

        # self.inner_inner_frame =ctk.CTkFrame(self.tab_view1)
        # self.inner_inner_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        cols = ([i for i in range(13)])
        cols[0]=''
        self.treeview = ttk.Treeview(self.inner_frame2, show='headings', columns=cols )
        self.treeview.grid(row=0, rowspan=9, column =0, padx=10, pady=10, columnspan=13, sticky='nsew')
       # grid(row = 1, rowspan=11, column=0, padx=10, pady=(2,30), sticky="nsew")
        
        self.treeview.configure(padding=20, selectmode='extended')

        for colname in cols:
            self.treeview.column(colname, anchor='center', width=40)
            self.treeview.heading(colname, text=colname)
        

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

        col=0
        # for key in my_dict.keys():
        #     for value in my_dict[key]:
        #         if col == 0:
        #             self.treeview.insert(parent="", index="end", id=key, text="", values=tuple(my_dict[key][0]), tags=('first_column'))
        #     self.treeview.insert(parent="", index="end", id=key, text="", values=tuple(my_dict[key][1:]), tags=('green'))

        style = ttk.Style()
        style.theme_use('default')
        # self.treeview.tag_bind()


        # Apply the custom style to the Treeview widget
        # self.treeview.configure(style="Custom.Treeview")
        # Customize the Treeview widget style
        style.configure("Treeview", background="#646668", fieldbackground="#646668", foreground="white")

        # Change the font of the Treeview widget
        # style.configure("Treeview", font=("Helvetica", 12))

        # # Change the background color of the Treeview widget
        # style.configure("Treeview", background="lightgray")

        # # Change the foreground color of the Treeview widget
        # style.configure("Treeview", foreground="black")

        # Change the row height of the Treeview widget
        style.configure("Treeview", rowheight=40)

        # Change the color of the selected item
        style.map("Treeview", background=[("selected", "#1466BD")], foreground=[("selected", "white")])


        self.treeview.bind("<Double-1>", self.on_double_click)


    def on_double_click(self, event):
        self_iid = self.treeview.focus()
        selected_values = self.treeview.item(self_iid)

        column = self.treeview.identify_column(event.x)
        colindex = int(column[1:])-1

        selected_text = ''
        if column == '#0':
            selected_text = selected_values.get('text')[colindex]
        else:
            selected_text = selected_values.get('values')[colindex]


        column_box = self.treeview.bbox(self_iid, column)
        self.entry = ttk.Entry(self.treeview, width=column_box[2])
        self.entry.place(x = column_box[0], y=column_box[1], w=column_box[2], h=column_box[3] )


        self.entry.insert(0, selected_text) #insert cell text to the entry
        self.entry.select_range(0, tk.END) # select the whole text of the entry
        self.entry.focus()

        self.entry.column_index = colindex
        self.entry.item_iid = self_iid

        self.entry.bind("<FocusOut>", self.on_focus_out) # to disappear the entry widget on focus out

        self.entry.bind("<Return>", self.on_enter_pressed)
    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        new_value = event.widget.get()
        print(new_value)

        selected_iid = event.widget.item_iid

        selected_column_index = event.widget.column_index


        self.current_value = self.treeview.item(selected_iid).get('values')
        self.current_value[selected_column_index]= new_value
        self.treeview.item(selected_iid, values=self.current_value)
        
        event.widget.destroy()





class rightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.columnconfigure(0, weight=1)

        self.combo_data_category = ctk.CTkComboBox(self, values=['Select Data Category','Extraction Layout', 'Assay Layout', 'Raw Data'])
        self.combo_data_category.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.combo_google_sheet_url = ctk.CTkComboBox(self, values=['Google Sheet Url','Dark', 'Light'])
        self.combo_google_sheet_url.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.combo_redcap_project = ctk.CTkComboBox(self, values=['Redcap Project'])
        self.combo_redcap_project.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('GPyRed')
        self.geometry('700x500')
    
        # self.resizable(width=True, height=True)
        
        
        
        self.mainFrame = ctk.CTkFrame(self)
        self.rowconfigure(0, weight=1) 
        self.columnconfigure(0, weight=1)

        self.mainFrame.grid(row=0, column=0,sticky="nswe")

        self.mainFrame.grid_columnconfigure((0, 2), weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=10)
        self.mainFrame.grid_rowconfigure(0, weight=1)

        self.frame1 = leftFrame(self.mainFrame) # Calling class leftFrame
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.18, relheight=0.92)


        self.btn_side_bar = ctk.CTkButton(self.mainFrame, text="←", font=('Arial',25),text_color=('black', 'white'), hover=False, fg_color=('white', 'black'),command=lambda: self.show_hide_frame())
        self.btn_side_bar.place(relx=0.01, rely=0.95, relwidth=0.06, relheight=0.04)

        self.frame2 = middleFrame(self.mainFrame)  # Calling class middleFrame
        self.frame2.place(relx=0.21, rely=0.02, relwidth=0.54, relheight=0.92)

        self.frame3 = rightFrame(self.mainFrame)
        self.frame3.place(relx=0.77, rely=0.02, relwidth=0.22, relheight=0.94)


        self.frame_status= True
        self.frame1_start = 0.01
        self.frame2_start = 0.21
        self.frame3_start = 0.79
        self.frame1_width = 0.18
        self.frame2_width = 0.54
        self.frame3_width = 0.22
    def show_hide_frame(self):
        if self.frame_status:
            self.hide_frame()
            self.frame_status=False
        elif not self.frame_status:
            self.show_frame()
            self.frame_status=True
    def hide_frame(self):

        if self.frame1_start > -0.17:
            self.frame1_start -=0.05
            self.frame2_start -=0.05
            self.frame2_width +=0.05
            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.92)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.92)
            self.after(1, self.hide_frame) # calling function hide_frame after 100 milliseconds
            self.btn_side_bar.configure(text='→')

    def show_frame(self):
        
        if self.frame1_start < -0.01:
            self.frame1_start +=0.05
            self.frame2_start +=0.05
            self.frame2_width -=0.05

            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.92)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.92)
            self.after(1, self.show_frame)

            self.btn_side_bar.configure(text='←')






            


        


app = App()

app.mainloop()









