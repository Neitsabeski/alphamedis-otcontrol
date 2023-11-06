#################
#  FACTURATION  #
#  gui.py       #
#  Gardier S.   #
#################

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from files import FileT, TypeA, TypeB
from tools import *

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.file_a = None
        self.file_b = None
        self.title("Office Tarification Control")
        self.geometry("520x450")
        self.resizable(False, False)
        
        self.display()

    def display(self):

        ## Type A section

        # Label
        wl_origin_A = tk.Label(self, text="Alphamedis", anchor="w", font="-size 9 -weight bold")
        wl_origin_A.place(x=50, y=50, height=20, width=100)

        # Path
        wl_path_A = tk.Label(self, text="Select File A to compare.", anchor="w")
        wl_path_A.place(x=160, y=50, height=20, width=190)

        # Text Bloc
        wt_infos_A = tk.Text(self, state="disabled")
        wt_infos_A.place(x=50, y=80, height=100, width=420)

        wt_scrollbar_A = tk.Scrollbar(self, command=wt_infos_A.yview)
        wt_scrollbar_A.place(x=465, y=80, height=100, width=5)
        wt_infos_A.config(yscrollcommand=wt_scrollbar_A.set)

        # Button File
        wb_choose_A = tk.Button(self, text="Choose File", command=self.select_file(TypeA, wl_path_A, wt_infos_A))
        wb_choose_A.place(x=360, y=50, height=20, width=80)

        # Button Formalize
        wb_formalize_A = tk.Button(self, text="⚡", fg='red', command=lambda: self.formalize_files(TypeA))
        wb_formalize_A.place(x=450, y=50, height=20, width=20)

        CreateToolTip(wb_formalize_A, text = "Formalize")

        ## Type B section

        # Label
        wl_origin_B = tk.Label(self, text="Office Tarification", anchor="w", font="-size 9 -weight bold")
        wl_origin_B.place(x= 50, y=200, height=20, width=105)

        # Path
        wl_path_B = tk.Label(self, text="Select File B to compare.", anchor="w")
        wl_path_B.place(x= 160, y=200, height=20, width=190)

        # Text Bloc
        wt_infos_B = tk.Text(self, state="disable")
        wt_infos_B.place(x= 50, y=230, height=100, width=420)

        wt_scrollbar_B = tk.Scrollbar(self, command=wt_infos_B.yview)
        wt_scrollbar_B.place(x=465, y=230, height=100, width=5)
        wt_infos_B.config(yscrollcommand=wt_scrollbar_B.set)

        # Button File
        wb_choose_B = tk.Button(self, text="Choose File", command=self.select_file(TypeB, wl_path_B, wt_infos_B))
        wb_choose_B.place(x=360, y=200, height=20, width=80)

        # Button Formalize
        wb_formalize_B = tk.Button(self, text="⚡", fg='red', command=lambda: self.formalize_files(TypeB))
        wb_formalize_B.place(x=450, y=200, height=20, width=20)

        CreateToolTip(wb_formalize_B, text = "Formalize")

        ## Compare section
        
        # Button Compare
        wb_compare = tk.Button(self, text="Compare", command=self.compare_files)
        wb_compare.place(x=220, y=370, height=20, width=80)



    def compare_files(self):
        if self.file_a and self.file_b:
            FileT.compare_files(self.file_a, self.file_b)
        else:
            messagebox.showerror("Error - Compare", "You must select both files before compare.")

    def formalize_files(self, type_class):
        messagebox.showerror("Error - Formalize", "File is not correct to formalize.")

    def insert_log(self, data, text_widget):
        data += "----------------------------------------------------"
        text_widget.configure(state='normal')
        text_widget.insert(tk.END, data)
        text_widget.configure(state='disable')
        text_widget.see(tk.END)

    def select_file(self, type_class, label, text_widget):
        def inner():
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
            if file_path:
                if not file_path.lower().endswith('.csv'):
                    messagebox.showerror("Error - Selection", "You must select a .CSV File.")
                else:
                    file_name = os.path.basename(file_path)
                    truncated_path = (file_path[:25] + '...') if len(file_path) > 28 else file_path
                    label.config(text="{} ({})".format(truncated_path, file_name))
                    file = type_class(file_path)
                    file.show_infos()
                    data = file.read_file()
                    self.insert_log(data, text_widget)
                    if isinstance(file, TypeA):
                        self.file_a = file
                    elif isinstance(file, TypeB):
                        self.file_b = file
        return inner
