import  shutil as s
import os
pasta = rf'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim'
for subpastas, arquivos in os.walk(pasta):
    print(subpastas)
    print("_________________________")
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))