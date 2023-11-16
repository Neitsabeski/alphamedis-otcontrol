#################
#  FACTURATION  #
#  main.py      #
#  Gardier S.   #
#################

from gui import Interface

try:
    with open("credits.txt", "r") as file:
        print(file.read())
except:
    print("A L P H A M E D I S\n",
          "Gardier S.",
          "\n-------------------")
    

if __name__ == '__main__':
    app = Interface()
    app.mainloop()


