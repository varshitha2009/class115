import os
source="/Users/preetheegopinathan/Downloads/PRO-C113-Student-Boilerplate-main-main/main.txt"
destination="/Users/preetheegopinathan/Downloads/PRO-C113-Student-Boilerplate-main-main/newfile.txt"
os.rename(source,destination)
print("source path renamed to destination path successfully")