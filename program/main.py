#################
#  FACTURATION  #
#  main.py      #
#  Gardier S.   #
#################

from gui import Interface

with open("ascii_art.txt", "r") as file:
    ascii_art = file.read()
print(ascii_art)

if __name__ == '__main__':
    app = Interface()
    app.mainloop()
