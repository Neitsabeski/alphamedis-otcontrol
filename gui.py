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
from translations import *
from config import *
import datetime


class Interface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.file_a = TypeA()
        self.file_b = TypeB()
        self.title("Office Tarification Control")
        self.geometry("520x450")
        self.resizable(False, False)
        self.cfg = Config()
        self.count = 0
        self.lang = self.cfg.get_language()
        self.display()
        self.set_translation()
            
    def display(self):
        ## Type A section
        # Label
        self.wl_origin_A = tk.Label(self, text="Alphamedis", anchor="w", font="-size 9 -weight bold")
        self.wl_origin_A.place(x=50, y=50, height=20, width=100)
        # Path
        self.wl_path_A = tk.Label(self, text="Select File A to compare.", anchor="w")
        self.wl_path_A.place(x=160, y=50, height=20, width=190)
        # Text Bloc
        self.wt_infos_A = tk.Text(self, state="disabled")
        self.wt_infos_A.place(x=50, y=80, height=100, width=420)
        # Scrollbar
        wt_scrollbar_A = tk.Scrollbar(self, command=self.wt_infos_A.yview)
        wt_scrollbar_A.place(x=465, y=80, height=100, width=5)
        self.wt_infos_A.config(yscrollcommand=wt_scrollbar_A.set)
        # Button File
        self.wb_choose_A = tk.Button(self, text="Choose File", command=self.select_file(TypeA, self.wl_path_A, self.wt_infos_A))
        self.wb_choose_A.place(x=360, y=50, height=20, width=80)
        # Button Formalize
        self.wb_formalize_A = tk.Button(self, text="⚡", fg='red', command=lambda: self.formalize_files(TypeA, self.file_a, self.wt_infos_A))
        self.wb_formalize_A.place(x=450, y=50, height=20, width=20)
        CreateToolTip(self.wb_formalize_A, text = "Formalize")
        ## Type B section
        # Label
        self.wl_origin_B = tk.Label(self, text="Office Tarification", anchor="w", font="-size 9 -weight bold")
        self.wl_origin_B.place(x= 50, y=200, height=20, width=105)
        # Path
        self.wl_path_B = tk.Label(self, text="Select File B to compare.", anchor="w")
        self.wl_path_B.place(x= 160, y=200, height=20, width=190)
        # Text Bloc
        self.wt_infos_B = tk.Text(self, state="disable")
        self.wt_infos_B.place(x= 50, y=230, height=100, width=420)
        # Scrollbar
        wt_scrollbar_B = tk.Scrollbar(self, command=self.wt_infos_B.yview)
        wt_scrollbar_B.place(x=465, y=230, height=100, width=5)
        self.wt_infos_B.config(yscrollcommand=wt_scrollbar_B.set)
        # Button File
        self.wb_choose_B = tk.Button(self, text="Choose File", command=self.select_file(TypeB, self.wl_path_B, self.wt_infos_B))
        self.wb_choose_B.place(x=360, y=200, height=20, width=80)
        # Button Formalize
        self.wb_formalize_B = tk.Button(self, text="⚡", fg='red', command=lambda: self.formalize_files(TypeB, self.file_b, self.wt_infos_B))
        self.wb_formalize_B.place(x=450, y=200, height=20, width=20)
        CreateToolTip(self.wb_formalize_B, text="Formalize")
        ## Compare section
        self.wb_compare = tk.Button(self, text="Compare", command=self.compare_files)
        self.wb_compare.place(x=220, y=370, height=20, width=80)
        ## Translation section
        self.wb_translate = tk.Button(self, text="lang", command=self.change_translation)
        self.wb_translate.place(x=20, y=20, height=20, width=20)

    ## Display translation
    def set_translation(self):
        self.count += 1
        self.lang = self.cfg.get_language()
        if(self.count == 10):
            self.count = 0
            self.lang = "(e)"
        self.wb_translate.config(text=translations["language"][self.lang])
        self.wb_compare.config(text=translations["compare"]["text"][self.lang])
        self.wb_choose_A.config(text=translations["choose"]["text"][self.lang])
        if(self.file_a == None):
            self.wl_path_A.config(text=translations["path"][self.lang])
        self.wb_formalize_A.config(text=translations["formalize"]["text"][self.lang])
        CreateToolTip(self.wb_formalize_A, text=translations["formalize"]["hover"][self.lang])
        self.wb_choose_B.config(text=translations["choose"]["text"][self.lang])
        if(self.file_b == None):
            self.wl_path_B.config(text=translations["path"][self.lang])
        self.wb_formalize_B.config(text=translations["formalize"]["text"][self.lang])
        CreateToolTip(self.wb_formalize_B, text=translations["formalize"]["hover"][self.lang])
        self.title(translations["title"][self.lang])

    ## Action changing translation
    def change_translation(self):
        self.cfg.change_language()
        self.set_translation()
        if(self.cfg.get_debug()):
            print("change translation : {}".format(self.lang))

    ## Compare Files
    def compare_files(self):
        s_a = self.formalize_files(TypeA, self.file_a, self.wt_infos_A)
        s_b = self.formalize_files(TypeB, self.file_b, self.wt_infos_B)
        if( s_a.get_state() and s_b.get_state() ):
            FileT.compare_files(self.file_a, self.file_b)
        else:
            self.insert_log("Compare\n> Failed - {}".format(translations["compare"]["error"]["label"][self.lang]),self.wt_infos_A)
            self.insert_log("Compare\n> Failed - {}".format(translations["compare"]["error"]["label"][self.lang]),self.wt_infos_B)
            if(not self.cfg.get_debug()):
                messagebox.showerror(translations["compare"]["error"]["title"][self.lang], translations["compare"]["error"]["label"][self.lang])

    ##Formalize file
    def formalize_files(self, type_class, file, text_widget):
        res = file.formalize()
        if(res.get_state()):
            self.insert_log("Formalize\n> Succed - {}".format(res.get_message()),text_widget)
        else:
            self.insert_log("Formalize\n> Failed - {}".format(res.get_message()),text_widget)
            if(not self.cfg.get_debug()):
                messagebox.showerror(translations["formalize"]["error"]["title"][self.lang], "{} : {}".format(translations["formalize"]["error"]["label"][self.lang],type_class))
        return res

    ## Logs
    def insert_log(self, data, text_widget):
        now = datetime.datetime.now()
        time = "{}:{}:{}".format(now.hour, now.minute, now.second)
        break_line= "----------------------------------------------------"
        text_display = "{}\n{}\n{}".format(time, data, break_line)
        text_widget.configure(state='normal')
        text_widget.insert(tk.END, text_display)
        text_widget.configure(state='disable')
        text_widget.see(tk.END)

    ## Import File
    def select_file(self, type_class, label, text_widget):
        def inner():
            file_path = filedialog.askopenfilename(filetypes=[(translations["choose"]["dialog"]["files"]["csv"][self.lang], "*.csv"), (translations["choose"]["dialog"]["files"]["all"][self.lang], "*.*")])
            if file_path:
                if not file_path.lower().endswith('.csv'):
                    self.insert_log("Import\n> Failed - {}".format(translations["choose"]["error"]["label"][self.lang]),text_widget)
                    if(not self.cfg.get_debug()):
                        messagebox.showerror(translations["choose"]["error"]["title"][self.lang], translations["choose"]["error"]["label"][self.lang])
                else:
                    file_name = os.path.basename(file_path)
                    truncated_path = (file_path[:25] + '...') if len(file_path) > 28 else file_path
                    label.config(text="{} ({})".format(truncated_path, file_name))
                    file = type_class()
                    file.set_filepath(file_path)
                    if(self.cfg.get_debug()):
                        file.show_infos()
                    self.insert_log("Import\n> Succed\n{}".format(file.read_file_infos().get_message()),text_widget)
                    if isinstance(file, TypeA):
                        self.file_a = file
                    elif isinstance(file, TypeB):
                        self.file_b = file
        return inner
