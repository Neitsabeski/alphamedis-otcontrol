#################
#  FACTURATION  #
#  fichiers.py  #
#  Gardier S.   #
#################

import os
import datetime

class FileT:
    def __init__(self, filename):
        self.filename = filename

    def show_infos():
        print("N/A")

    def read_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)

        file_path = "N/A"
        file_size = "N/A"
        
        file_name = os.path.basename(self.filename)
        file_stats = os.stat(self.filename)
        last_modified = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        return "Path : {}\nFile name : {}\nDate last edit : {}\nRows : {}\nSize : {}\n".format(file_path, file_name, last_modified, line_count, file_size)

    '''
    def lire_fichier(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        return lines
    '''
    
    @staticmethod
    def compare_files(file_a, file_b):
        if isinstance(file_a, TypeA) and isinstance(file_b, TypeB):
            data_a = file_a.read_file()
            data_b = file_b.read_file()
            print("Compare files A and B :")
            print("\nFile A content : \n", data_a)
            print("\nFile B content : \n", data_b)
        else:
            messagebox.showerror("Erreur de comparaison", "Veuillez sélectionner un fichier de type A et un fichier de type B pour la comparaison.")


class TypeA(FileT):
    def __init__(self, filename):
        super().__init__(filename)

    def show_infos(self):
        print("TYPE A")

class TypeB(FileT):
    def __init__(self, filename):
        super().__init__(filename)

    def show_infos(self):
        print("TYPE B")
