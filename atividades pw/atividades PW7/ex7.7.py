import os 
import shutil
def createfile(myfile):
    with open(myfile, 'w') as file:
        file.writelines("Good morning")



namefile = input("Digite o nome do arquivo com a extensão: ")

createfile(namefile)
os.mkdir("temp")
shutil.move(namefile, 'temp')