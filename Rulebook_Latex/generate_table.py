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

file_contents = "\\begin{tabular}{|"

first = True
for item in list[0]:
    
    if first:
        first = False
    else:
        file_contents += "| "
    file_contents += str(item) + " "

list = list[1:]

#print(list)


file_contents += "|}\n"

for i, row in enumerate(list):
    if i == 0:
        file_contents += "\\hline"
    file_contents += "\t"
    first = True
    for item in row:
        if first:
            first = False
        else:
            file_contents += " & "
        file_contents += item
    file_contents += "\\\\"
    if i == 0:
        file_contents += "\\hline"
    file_contents += "\n"


file_contents += "\\hline\\end{tabular}"

print(file_contents)

#with open(filename + ".tex", "w") as text_file:
    #text_file.write(file_contents)

#print("Completed file '" + filename + ".tex'.")
