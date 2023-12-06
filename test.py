#################
#  FACTURATION  #
#  test.py      #
#  Gardier S.   #
#################

from response import Response
from files import FileT, TypeA, TypeB


################
### Functions ##
################

def print_line():
    print("\n----------------------------------\n")

## Empty liste
def empty_liste():
    liste = [
    ["1", "2", "3"],
    ["3.5","deux",""],
    ["quatre", "5", "6"],
    ["7", "huit", "9"],
    ]

    args = [
        [0, True],
        [1, False],
        [2, False],
    ]

    table_file = []

    for row in liste:
        state = all(row[e[0]].replace(".", "").isdigit() if e[1] else True for e in args) and not any(e == "" for e in row)
        if state:
            new_row = [row[e[0]] for e in args]
            if new_row not in table_file:
                table_file.append(new_row)

    print(table_file)

## Generic
def function(args, data):
    dialog = ["is numeric","is not numeric"]
    gen = (e for e in args if e[1])
    for e in gen:
        print(e)
        #print("args[{}] : {} {}".format(e[0], data[e[0]], ((dialog[0] if isnum(data[e[0]]) else dialog[1]) if e[1] else "") ))
        
def generic():
    print("- Generic -")
    
    table = ["zero","un","25","30.0","four","5.2","six","seven","84.0","nine"]
    args = [[
                [0,True],
                [2,True],
                [4,False],
                [6,True],
                [8,True]
            ],
            [
            ],
            [   [1,True],
                [3,True],
                [5,True],
                [7,True],
                [9,False]
            ]]
    for e in args:
        function(e, table)

    print_line()

## Numeric
def isnum(var):
    try:
        float(var)
        return True
    except:
        return False

def numeric():
    print("- Numeric -")
    element = [10,10.0,"10", "ten"]
    dialog = ["is numeric","is not numeric"]
    for e in element:
        print("> {} : {}".format(e, (dialog[0] if isnum(e) else dialog[1] )))
    print_line()
        
## Files
def files():
    print("- Files -\n")
    
    file_t = FileT()
    file_t.show_infos()

    print_line()

    file_a = TypeA()
    file_a.show_infos()

    print_line()
    
    file_b = TypeB()
    file_b.show_infos()

    print_line()

## Formalize & Response
def formalize_response():
    print("- Formalise & response -\n")
    
    res = Response()
    print("1. No File\nres : [ {} ; {} ; {} ]".format(res.get_state(), res.get_message(), res.get_data()))

    print_line()

    file = TypeB()
    file.show_infos()
    res = file.formalize()
    print("2. Empty File\nres : [ {} ; {} ; {} ]".format(res.get_state(), res.get_message(), res.get_data()))

    print_line()

    file = TypeB()
    file.set_filepath("../input/OfficeTarification/Alphamedis2.csv")
    file.show_infos()
    res = file.formalize()
    print("3. File with path\nres : [ {} ; {} ; {} ]".format(res.get_state(), res.get_message(), res.get_data()))

    print_line()


############
### Main ###
############

print("-- Main --\n- Tests  -\n")

empty_liste()
#generic()
#numeric()
#files()
#formalize_response()
