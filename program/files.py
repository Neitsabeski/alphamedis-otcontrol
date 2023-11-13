#################
#  FACTURATION  #
#  files.py     #
#  Gardier S.   #
#################

import os
import datetime

def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

class FileT:

    static_cfg = None
    
    def __init__(self, filepath):
        self.filepath = filepath

    def formalize(self):
        print("Formalize T")

    def get_type(self):
        return(self.type)

    def show_infos():
        print("N/A")

    def read_file_infos(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)

        file_path = self.filepath        
        file_name = os.path.basename(self.filepath)
        file_stats = os.stat(self.filepath)
        last_modified = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_size = truncate_float(file_stats.st_size / (1024 * 1024), 3)

        return "Path :\t{}...\nName :\t{}\nDate :\t{}\nRows :\t{}\nSize :\t{}Mo\n".format(file_path[0:40], file_name, last_modified, line_count, file_size)

    def read_file_rows(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
        return lines

    
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
    def __init__(self, filename):
        super().__init__(filename)
        self.type = "TypeA"
        
    def formalize(self):
        state = False
        print("Formalize TypeA")
        try:
            state = False
        except:
            state = False
        return state

    def show_infos(self):
        print("TYPE A\n",self.filepath)

class TypeB(FileT):
    def __init__(self, filename):
        super().__init__(filename)
        self.type = "TypeB"

    def formalize(self):
        state = False
        if(FileT.static_cfg.get_debug()):
            print("Formalize TypeB")
        try:
            file = self.read_file_rows()
            table_file = []
            table_treatment = []
            split = ";"
            for row in file:
                row_temp = row.split(split)
                try:
                    int(row_temp[0])
                    new_row = []
                    new_row.append(row_temp[0])
                    new_row.append(row_temp[5])
                    new_row.append(row_temp[3])
                    new_row.append(row_temp[7])
                    if(new_row not in table_file):
                        table_file.append(new_row)
                except:
                    error = 1
            
            print("\nTable:")
            self.show_matrix(table_file)
            state = True
        except:
            state = False
        return state

    def show_matrix(self, matrix):
        for row in matrix :
            print(row)
    
    def show_infos(self):
        print("TYPE B\n", self.filepath)
