from tkinter import *
from tkinter import ttk, Frame
from tkinter.messagebox import showinfo
from decor_models import validate_couter, session_number, name_func_panel, session_counter
from tkinter import filedialog

class Admin_app(ttk.Frame):
    def __init__(self, enum):
        ttk.Frame.__init__(self)

        ttk.Style().configure(".",  font="Times 12")

        self.lst = ["admin", "admin"]
        self.spinbox_var = StringVar()
        self.check_per_but = IntVar()
        self.columns = ("first_name", "last_name", "email")
        self.languages=["Python", "HTML", "C", "Tcl", "R"]
        
        self.usr_data = [("first_name", "last_name", "first_last_name@email.com"), \
                         ("first_name", "last_name", "first_last_name@email.com"), \
                            ("first_name", "last_name", "first_last_name@email.com")]


        if session_number == 0:
            self.setup_login_panel()
    
    def setup_login_panel(self):
        self.ramka = ttk.Frame(self, borderwidth=1, relief=SOLID)
        self.ramka.pack(expand=1, anchor="nw", padx=5, pady=5, fill=BOTH)

        self.frame1 = ttk.Frame(self.ramka, borderwidth=1, relief=SOLID, padding=[3, 3])
        self.frame1.place(anchor="center", relx=0.5, rely=0.5, height=150, width=278)
        
        self.frame2 = ttk.Frame(self.ramka, borderwidth=1, relief="")
        self.frame2.place(anchor="n", relx=.5, rely=.01, relheight=.22, relwidth=.99)
        
        self.frame3 = ttk.Frame(self.ramka, borderwidth=1, relief="")
        self.frame3.place(anchor="s", relx=0.5, rely=0.99, relheight=.22, relwidth=.99)
        
        self.mini_frame1 = ttk.Frame(self.frame1)
        self.mini_frame1.pack(side=TOP)
        self.mini_frame2 = ttk.Frame(self.frame1)
        self.mini_frame2.pack(expand=1, anchor="center")
        self.mini_frame3 = ttk.Frame(self.frame1)
        self.mini_frame3.pack(expand=1, anchor="center")

        self.name_label1 = ttk.Label(self.mini_frame1, text="Логин", foreground="")
        self.name_label2 = ttk.Label(self.mini_frame2, text="Пороль", foreground="")
        self.name_entry1 = ttk.Entry(self.mini_frame1, width=68, font=("Times", 12))
        self.name_entry2 = ttk.Entry(self.mini_frame3, show="*", width=68, font=("Times", 12))
        self.button1 = ttk.Button(self.frame1, text="Вход", width=12, command=self.check_login_password)


        self.cbut_check = ttk.Checkbutton(self.mini_frame3, variable=self.check_per_but, command=self.show_password_check)
        self.cbut_check.pack(side=RIGHT, expand=1, anchor="e")

        self.name_label1.pack(side=TOP, anchor="center")
        self.name_entry1.pack(anchor="center", padx=5)
        self.name_label2.pack(anchor="center")
        self.name_entry2.pack(anchor="center", padx=5)
        
        self.button1.pack(side=BOTTOM, anchor="center", ipady=2, pady=5)

        self.reg_but_help = ttk.Button(self.frame3, text="?", command=self.info_default_log, width=3)
        self.reg_but_help.pack(expand=1, anchor="sw")
    
    def setup_admin_panel(self):
        self.main_frame = ttk.Frame(self, borderwidth=1, relief="solid")
        self.main_frame.pack(fill=BOTH, expand=True, anchor="nw", padx=2, pady=2)

        self.first_frame = ttk.LabelFrame(self.main_frame, borderwidth=1, relief=SOLID, text="Меню")
        self.second_frame = ttk.LabelFrame(self.main_frame, borderwidth=1, relief=SOLID, text="Панель")

        self.settigs_but = ttk.Button(self.first_frame, text="Настройки", command=self.settings_panel)
        self.contents_but = ttk.Button(self.first_frame, text="Контент", command=self.contents_panel)
        self.info_but = ttk.Button(self.first_frame, text="Информация", command=self.info_panel)

        self.first_frame.place(anchor="nw", relheight=.99, relwidth=.29, relx=.001, rely=.001)
        self.second_frame.place(anchor="ne", relheight=.99, relwidth=.69, relx=.99, rely=.001)

        self.first_frame.columnconfigure(index=0, weight=1)
        self.settigs_but.grid(row=0, sticky="ew")
        self.contents_but.grid(row=1, sticky="ew")
        self.info_but.grid(row=3, sticky="ew")

    def info_default_log(self):
        showinfo(title="Информация", message="Логин: admin / Пороль: admin")
    
    def show_password_check(self):
        if self.check_per_but.get() == 0:
            self.name_entry2.config(show="*")
        else:
            self.name_entry2.config(show="")

    @validate_couter
    def check_login_password(self):
        self.login = self.name_entry1.get()
        self.password = self.name_entry2.get()
        if self.login == self.lst[0] and self.password == self.lst[1]:
            self.delete_app()
            refresh()
        else:
            self.name_label1.config(foreground="red")
            self.name_label2.config(foreground="red")

    def delete_app(self):
        self.widgets = self.winfo_children()
        for widget in self.widgets:
            widget.destroy()

    
    @name_func_panel
    def settings_panel(self):
        self.widgets = self.second_frame.winfo_children()
        for widget in self.widgets:
            widget.destroy()

        for i in range(2): self.columnconfigure(index=i, weight=1)
        for j in range(4): self.rowconfigure(index=j, weight=1)

        self.label = ttk.Label(self.second_frame, textvariable=self.spinbox_var)
        self.label.grid(row=0, column=1)

        self.spinbox = ttk.Spinbox(self.second_frame, textvariable=self.spinbox_var, values=self.languages)
        self.spinbox.grid(row=0, column=0)

    @name_func_panel
    def contents_panel(self):
        self.widgets = self.second_frame.winfo_children()
        for widget in self.widgets:
            widget.destroy()

        self.pole_path = ttk.Entry(self.second_frame)
        self.pbut_path = ttk.Button(self.second_frame, text="...", command=self.open_contents_path)

        self.pole_path.grid(row=0, column=0)
        self.pbut_path.grid(row=0, column=1)

    def info_panel(self):
        self.widgets = self.second_frame.winfo_children()
        for widget in self.widgets:
            widget.destroy()

        for i in range(4): self.columnconfigure(index=i, weight=1)

        self.label_info = ttk.Label(self.second_frame, text="Выберите файл описания")
        self.pbut_file = ttk.Button(self.second_frame, text="...", command=self.open_info_file)

        self.label_info.grid(row=0)
        self.pbut_file.grid(row=1)

        self.table_1 = ttk.Treeview(self.second_frame, columns=self.columns, show="headings", padding=[5, 5])
        self.table_1.grid(row=2, padx=5, pady=5, ipadx=5, ipady=5, rowspan=4, columnspan=3, sticky="w")
        
        self.table_1.heading("first_name", text="Имя")
        self.table_1.heading("last_name", text="Фамилия")
        self.table_1.heading("email", text="Email")

        self.table_1.column("#1", stretch=False, width=100)
        self.table_1.column("#2", stretch=False, width=90)
        self.table_1.column("#3", stretch=False, width=175)
        
        for person in self.usr_data:
            self.table_1.insert("", END, values=person)
    
    def open_info_file(self):
        self.info_file = filedialog.askopenfilename()
        if self.info_file != "":
            with open(self.info_file, "r") as file:
                txt_info = file.read()
            self.label_info.config(text=f"{txt_info}")
    
    def open_contents_path(self):
        self.contents_path = filedialog.askdirectory()
        self.pole_path.insert(0, self.contents_path)

if __name__ == "__main__":
    root = Tk()
    root.title("login")
    
    app_1 = Admin_app(root)
    app_1.pack(fill="both", expand=True)
    
    @session_counter
    def refresh():
        app_1.setup_admin_panel()

    root.geometry("600x575+550+275")
    root.resizable(False, False)
    root.mainloop()