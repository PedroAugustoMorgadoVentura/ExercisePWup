#chat gpt usa muito função pra isso, vou usar isso mesmo pq achei mais organizado e fácil de entender. 
import os


def renomear(file):
    with open(file, "r"):
       
        name, extension = os.path.splitext(file)


        newname = f"{name}renamed{extension}"
        os.rename(file, newname)
        return newname
    


print(renomear('file_renomeado.txt'))





