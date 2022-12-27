import os
import shutil
import subprocess
import time

""" 
fazer o teste se o arquivo criado tem um caminho existente 
caso ainda não exista o caminho especificado significa que o mesmo 
foi anexado em uma pasta, sendo assim é necessário criar o caminho 
no novo diretório 
"""



class atualization_dic:

    def transfer(rotina1):
        try:
            # completed = subprocess.run(["powershell", "-Command", rotina1], capture_output=True)
            completed = subprocess.run([])
        except:
            print(f"a rotinha: {rotina1} não deu certo")
    def created_event(event):

        """
        inicialmente iremos testar se a pasta local do evento já existe ou não
        isso porque o evento de criação não mostra caso seja criado um diretorio (pasta)
        sempre retorna o arquivo adicionado
        """


        """ funçao para encontrar as divições do Path enviado
        lst representa uma lista com a posição de todas as divisões do Path"""

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim1"

        c = '\\'
        lst = []
        for pos, char in enumerate(event):
            if (char == c):
                lst.append(pos)


        # iremos testar a existencia do caminho final do arquivo no novo diretorio
        n = len(lst)-1
        # print(n)
        # print(event[(lst[n]+1):len(event)])
        # print(event[lst[0]:lst[n]+1])

        """
        o PowerShell tem um grande problema para nomes de pastas e arquivos que contem espaço no nome
        para solucionar esse problema é muito importante passar os caminho entre aspas duplas 
        assim ele entende esses espaços em branco 
        """
        teste = os.access(fr"{caminho_dir_copia}{event[lst[4]:lst[n]]}",os.F_OK)

        if teste:
            print('aqui vamos fazer a transferencia do arquivo via powershell')
            rotina1 = f'Copy-Item -Path "{event[lst[0]:lst[n]+1]}{event[(lst[n]+1):len(event)]}" -Destination "{caminho_dir_copia}{event[lst[4]:lst[n]]}" -Recurse -Force -Passthru'
            print(rotina1)
            atualization_dic.transfer(rotina1)

        else:
            print("vamos ter criar o caminho no novo path para isso precisamos criar o caminnho")

            k = 4
            while k != n:

                if (os.access(rf"{caminho_dir_copia}{event[lst[4]:lst[k+1]]}",os.F_OK)):
                    print("a pasta já existe")
                    print(rf"{caminho_dir_copia}{event[lst[4]:lst[k+1]]}")
                    k += 1

                else:

                    os.mkdir(rf"{caminho_dir_copia}{event[lst[4]:lst[k+1]]}")
                    k += 1

                #event[lst[0]:lst[n] + 1]}{event[(lst[n] + 1):len(event)]

            rotina1 = f'Copy-Item -Path "{event}" -Destination "{caminho_dir_copia}{event[lst[4]:lst[n]]}" -Recurse -Force -Passthru'
            print(rotina1)
            atualization_dic.transfer(rotina1)


    def deleted_event( event):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim"

        c = '\\'
        lst = []
        for pos, char in enumerate(event):
            if (char == c):
                lst.append(pos)

        n = len(lst) - 1

        """
        1) quando utilizamos a biblioteca OS temos problema para excluir os dados, sempre da erro de acesso 
        2) Com o powerShell não temos o problema de acesso para excluir arquivos e pastas 
        3) na linha de comando shell eu necessito usar a função ( -recurse) para que o comando esteja habito para 
        excluir pastas e arquivos  
        """
        rotina2 = f'Remove-item -path "{caminho_dir_copia}{event[lst[4]:len(event)]}" -recurse'
        atualization_dic.transfer(rotina2)

        # try:
        #     os.remove(f"")
        #     print("removido")
        # except OSError as e:
        #     print(f"Error:{e.strerror}")
        #     pass
        #


    def modified_event(event):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim"

        c = '\\'
        lst = []
        for pos, char in enumerate(event):
            if (char == c):
                lst.append(pos)

        n = len(lst) - 1

        teste1 = os.path.isfile(event)
        teste2 = os.access(fr"{caminho_dir_copia}{event[lst[4]:len(event)]}",os.F_OK)

        if teste1 and teste2:
            rotina3 = f'Copy-Item -Path "{event}" -Destination "{caminho_dir_copia}{event[lst[4]:lst[n]]}" -Recurse -Force -Passthru'
            print(rotina3)
            atualization_dic.transfer(rotina3)



        print('coisa')

if __name__ == '__main__':
    ocorrencia = r"C:\Users\ifrtef\Desktop\scim\archive\källscim cvx\18a-52-00140-05 Set screw.doc"
    atualization_dic.created_event(ocorrencia)

