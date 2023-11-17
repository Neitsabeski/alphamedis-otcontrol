#################
#  FACTURATION  #
#  files.py     #
#  Gardier S.   #
#################

import os
import datetime
import pandas as pd
from response import Response
from config import Config
from tools import Tools


class FileT:

    static_cfg = Config()
    
    def __init__(self):
        self.filepath = None
        self.type = "TypeT"

    ## Getter & Setter

    def get_type(self):
        return(self.type)

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, path):
        self.filepath = path

    def set_type(self, t):
        self.type = t

    ## Display infos in console

    def show_matrix(self, matrix):
        for row in matrix :
            print(row)

    def show_infos(self):
        print("File \n- Type : {}\n- Path :'{}'".format(self.type, self.filepath))

    ## Reading file

    def read_file_infos(self):
        res = Response()
        if(self.get_filepath() == None):
            res.set_response(False, "No file path", None)
            return res
        try:
            with open(self.get_filepath(), 'r') as file:
                lines = file.readlines()
                line_count = len(lines)
            file_path = self.filepath        
            file_name = os.path.basename(self.filepath)
            file_stats = os.stat(self.filepath)
            last_modified = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            file_size = Tools.truncate_float(file_stats.st_size / (1024 * 1024), 3)
            res.set_response(True, "Path :\t{}...\nName :\t{}\nDate :\t{}\nRows :\t{}\nSize :\t{}Mo".format(file_path[0:40], file_name, last_modified, line_count, file_size), None)
        except:
            res.set_response(False, "Error Read file infos", None)
        return res
    
    def read_file_rows(self):
        res = Response()
        if(self.get_filepath() == None):
            res.set_response(False, "No file path", None)
            return res
        try:
            lines = []
            with open(self.get_filepath(), 'r') as file:
                lines = file.readlines()
                res.set_response(True, "Read file rows : {}".format(len(lines)), lines)
        except:
            res.set_response(False, "Error Read file rows", None)
            if(self.static_cfg.get_debug()):
                print(res.get_message())
        return res

    @staticmethod
    def row_control(args, row):
        res = Response()
        new_row = []
        split = ";"
        try:
            row_temp = row.split(split)
            new_row = [row_temp[e[0]] for e in args if Tools.isnumeric(row_temp[e[0]]) == e[1] and row_temp[e[0]] != "" ]
            if(len(new_row) == len(args)):
                res.set_response(True, "Success no way", new_row)
        except Exception as error:
            print("Error")
        return res
    
    @staticmethod
    def extract_content(args, res):
        file = res.get_data()
        table_file = []
        for row in file:
            res_row = FileT.row_control(args, row)
            new_row = res_row.get_data()
            if(res_row.get_state()):
                table_file.append(new_row)
        if(FileT.static_cfg.get_debug()):
            print("\nTable:")
            for row in table_file :
                print(row)
        nb_row = len(table_file)
        res.set_response(True, "Rows kept : {}".format(nb_row), table_file)
        return res
        
    @staticmethod
    def compare_files(file_a, file_b):
        if isinstance(file_a, TypeA) and isinstance(file_b, TypeB):
            data_a = file_a.read_file_infos()
            data_b = file_b.read_file_infos()
            print("Compare files A and B :")
            print("\nFile A content : \n", data_a)
            print("\nFile B content : \n", data_b)
        else:
            messagebox.showerror("Erreur de comparaison", "Veuillez sélectionner un fichier de type A et un fichier de type B pour la comparaison.")


class TypeA(FileT):
    def __init__(self):
        super().__init__()
        self.set_type("TypeA")
        
    def formalize(self):
        if(FileT.static_cfg.get_debug()):
            print("Formalize TypeA")
        res = self.read_file_rows()
        if(res.get_state() == False):
            return res
        args = [
            [0,True],
            [5,False],
            [3,False],
            [7,False]]
        return FileT.extract_content(args, res)

class TypeB(FileT):
    def __init__(self):
        super().__init__()
        self.set_type("TypeB")


    def formalize(self):
        if(FileT.static_cfg.get_debug()):
            print("Formalize TypeB")
        res = self.read_file_rows()
        if(res.get_state() == False):
            return res
        args = [
            [0,True],
            [5,False],
            [3,False],
            [7,False]]
        res = FileT.extract_content(args, res)

        df = pd.DataFrame(res.get_data(),columns=['mut', 'date', 'niss', 'cout'])
        df['cout'] = df['cout'].str.replace(',','.')
        df['cout'] = df['cout'].astype(str).astype(float) 
        df2 = df.groupby(['date','mut','niss'],as_index=False).agg({'cout': 'sum'})

        if(FileT.static_cfg.get_debug()):
            print(df)
            print(df2)
                
        return res

    def row_inside():
        res = Response()
        return res
