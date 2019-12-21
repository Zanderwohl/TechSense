import pandas as pd
import numpy as np

def paragraph(header, content):
    paragraph = "\n\n\\paragraph{" + header + "}\n"
    paragraph += content
    return paragraph

filename = input("filename:")

list = pd.read_csv(filename + ".csv", header=None)
list = np.array(list)

#print(list)

file_contents = "\\begin{tabular}{"

first = True
for item in list[0]:
    
    if first:
        first = False
    else:
        file_contents += "| "
    file_contents += item + " "
    
list = list[1:]

#print(list)


file_contents += "}\n"

for row in list:
    file_contents += "\t"
    first = True
    for item in row:
        if first:
            first = False
        else:
            file_contents += " & "
        file_contents += item
    file_contents += "\\\\ \\hline"
    file_contents += "\n"


file_contents += "\\end{tabular}"

print(file_contents)

#with open(filename + ".tex", "w") as text_file:
    #text_file.write(file_contents)

#print("Completed file '" + filename + ".tex'.")
