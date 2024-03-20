import os

directory = "/home/lboullot/minidataset"

checkfile_path = os.path.join(directory, "checkfile")
with open(checkfile_path, "w") as checkfile:
    for direct in os.listdir(directory):
        dir_path = os.path.join(directory, direct)
        if os.path.isdir(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith(".tex"):
                    filepath = os.path.join(dir_path, filename)
                    with open(filepath, "r", encoding="utf-8", errors = 'replace') as file:
                        Tableau=False
                        content = ""
                        for line in file:
                            if "\\begin{tabular}" in line:
                                content += "\\leavevmode\\pdfstartlink\n"
                                content += line + "\n"
                                if Tableau == False :
                                    checkfile.write(filepath+"\n")
                                    Tableau == True
                            elif "\\end{tabular}" in line:
                                content += line + "\n"
                                content += "\\pdfendlink\n"
                            else:
                                content += line + "\n"
                    new_filepath = os.path.join(directory+"/minidatasetbis", filename + "v2.tex")
                    with open(new_filepath, "w") as new_file
                        new_file.write(content)
