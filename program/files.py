#################
#  FACTURATION  #
#  files.py     #
#  Gardier S.   #
#################

import os
import datetime
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

    ## Files operation

    @staticmethod
    def extract_content(args, res):
        try:
            file = res.get_data()
            table_file = []
            split = ";"
            for row in file:
                row_temp = row.split(split)

                # requires numeric
                gen = (e for e in args if e[1])
                state = False
                for e in gen:
                    if(Tools.isnumeric(row_temp[e[0]])):
                        state = True
                
                '''
                # requires not null
                if(row_temp[0] == "" or row_temp[5] == "" or row_temp[3] == "" or row_temp[7] == "" ):
                    continue
                '''
                
                if(state):
                    new_row = []

                    for e in args:
                        new_row.append(row_temp[e[0]])

                    if(new_row not in table_file):
                        table_file.append(new_row)

            if(FileT.static_cfg.get_debug()):
                print("\nTable:")
                for row in table_file :
                    print(row)
            nb_row = len(table_file)
            res.set_response(True, "Rows kept : {}".format(nb_row), table_file)
        except:
            res.set_response(False, "Error Formalizing", None)
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
        res = Response()
        print("Formalize TypeA")
        try:
            res.set_message("Success formalising")
        except:
            res.set_message("Error formalising")
        return res

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
        return FileT.extract_content(args, res)
        

    '''
    def formalize(self):
        if(FileT.static_cfg.get_debug()):
            print("Formalize TypeB")
        res = self.read_file_rows()
        if(res.get_state() == False):
            return res
        try:
            file = res.get_data()
            table_file = []
            split = ";"
            for row in file:
                row_temp = row.split(split)
                if(not Tools.isnumeric(row_temp[0])):
                    continue
                if(row_temp[0] == "" or row_temp[5] == "" or row_temp[3] == "" or row_temp[7] == "" ):
                    continue
                int(row_temp[0])
                new_row = []
                new_row.append(row_temp[0])
                new_row.append(row_temp[5])
                new_row.append(row_temp[3])
                new_row.append(row_temp[7])
                if(new_row not in table_file):
                    table_file.append(new_row)
            if(FileT.static_cfg.get_debug()):
                print("\nTable:")
                self.show_matrix(table_file)
            nb_row = len(table_file)
            res.set_response(True, "Rows kept : {}".format(nb_row), table_file)
        except:
            res.set_message("Error formalising")
        return res
    '''
