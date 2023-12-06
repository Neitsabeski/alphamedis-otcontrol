#################
#  ASCII ART    #
#  ascii.py     #
#  Gardier S.   #
#################

'''

    [aa bb     [[['a',2],[' ',1],['b',2]],    [[aa bb],
                                               [],
     bb  a] =>  [['b',2],[' ',2],['a',1]]] =>  [bb  a]]
     
'''

DEBUG = True

def display_matrix(matrix):
    print(matrix)

def open_ascii(path):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except:
        print("Error - open_file")

def export_formula(matrix, path):
    try:
        with open(path, 'w') as file:
            file.write(matrix)
    except:
        print("Error - export_file")

def count_successive_characters(line):
    counter = 1
    formula = []
    if not line:
        return formula
    
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            counter += 1
        else:
            formula.append([line[i - 1], counter])
            counter = 1
    formula.append([line[-1], counter])
    return formula
    
def ascii_to_formula(matrix):
    formula = []
    for line in matrix:
        row_formula = count_successive_characters(line)
        formula.append(row_formula)
    return formula

def formula_to_ascii(formula):
    text = ""
    for row in formula:
        if row == []:
            text += '\n'
        for c in row:
            for i in range(0,c[1]):
                text += c[0]
    return text

file = open_ascii("credits.txt")
formula = ascii_to_formula(file)
ascii_text = formula_to_ascii(formula)

export_formula(formula, "formula.txt")
display_matrix(ascii_text)


