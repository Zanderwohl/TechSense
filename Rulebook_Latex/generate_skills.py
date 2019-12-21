import pandas as pd
import numpy as np

def paragraph(header, content):
    paragraph = "\n\n\\paragraph{" + header + "}\n"
    paragraph += content
    return paragraph

list = pd.read_csv('skills.csv')
list = np.array(list)

#print(list)

list = list[list[:,0].argsort()]

#print(list)

skills_feelings = []
skills_lasers = []
abilities = []

for row in list:
    if(row[2] == "feelings"):
        skills_feelings.append(row[0:2])
    if(row[2] == "lasers"):
        skills_lasers.append(row[0:2])
    if(row[2] == "ability"):
        abilities.append(row[0:2])

file_contents = "%Contains a list of all skills an abilities"
file_contents +="\n%Each list should be in alphabetical order."
file_contents += "\n%Generated based on data in 'skills.csv'"
file_contents += "\n%And assembled via generate_skills.py"

file_contents += "\n\n\\section{List of \\skillC s}"

file_contents += "\n\n\\subsection{\\feelingsC}"
for skill in skills_feelings:
    file_contents += paragraph(skill[0], skill[1])

file_contents += "\n\n\\subsection{\\lasersC}"
for skill in skills_lasers:
    file_contents += paragraph(skill[0], skill[1])

file_contents += "\n\n\\section{List of \\abilityPC}"
for ability in abilities:
    file_contents += paragraph(ability[0], ability[1])

#print(file_contents)

with open("skillslist.tex", "w") as text_file:
    text_file.write(file_contents)

print("Completed file 'skillslist.tex'.")
