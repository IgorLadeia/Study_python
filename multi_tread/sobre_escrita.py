import time
import subprocess
import multiprocessing
import pandas as pd
import os

tempo00 = time.time()

chassis_bus = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_bus'
chassis_truck = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_truck'

rotina10 = f"Get-ChildItem -Path {chassis_bus} -Force -Recurse"
rotina20 = f"Get-ChildItem -Path {chassis_truck} -Force -Recurse"

# -Recurse
# rotina1 = f"Copy-Item -Path {chassis_bus} -Destination {destino} -Recurse -Force -Passthru"
# rotina2 = f"Copy-Item -Path {chassis_truck} -Destination {destino} -Recurse -Force -Passthru"

'''
a transferencia é realizada via power sheel, para chamar qualquer função do power sheel pelo python 
é necessario a utilização a biblioteca SUBPROCESSING, com ela podemos não somente chamar o powershel como 
utilizar ooutros softwares 

as rotinas que estari fazendo é basicamente  os :
    Copy-Item -Path "{caminho_origem}" -Destination "{caminho_destino}" -Recurse -Force -Passthru' que força a 
sobre escreita dos arquivos e seus metadados
 
'''


def transferencia100(rotina):
    try:
        completed = subprocess.run(["powershell", "-Command", rotina], capture_output=True)
    except:
        print(f"a rotinha: {rotina} não deu certo")


def transferencia200(rotina):
    try:
        completed = subprocess.run(["powershell", "-Command", rotina], capture_output=True)
    except:
        print(f"a rotinha: {rotina} não deu certo")


def transferencia300(rotina):
    try:
        completed = subprocess.run(["powershell", "-Command", rotina], capture_output=True)
    except:
        print(f"a rotinha: {rotina} não deu certo")


def transferencia400(rotina):
    try:
        completed = subprocess.run(["powershell", "-Command", rotina], capture_output=True)
    except:
        print(f"a rotinha: {rotina} não deu certo")


'''
a função escreva esta sendo utilizada para o tratamento de dados após a leitura dos diretórios 
1 --> transforma-mos todos os dados que retornaram da função anterior em string
2 --> retirar as quebras de pagina (\n) e criar uma lista de linhas para isso utiliza-mos a função split
3 --> set das listas
4 --> agora iremos fazer o separa cada linha em uma lista de palavras utilizando o line.split(None)
5 --> iremos percorrer as cada lista de palavras para tratar o dado
5.1 --> utilizamos o for com (i,line) para pular as primeiras linhas indesejadas 
5.2 --> o nome do diretorio esta nas linhas que contem a palavra ("Diret\\xa2rio:") para tratar essas linhas utilizaremos 
a fução try, caso encontrei essa linha ira separar apenas o nome do diretorio 
5.3 --> na linha [[if (ver_fal and i > 5 and len(exp) > 4):]] eu estou pulando as 5 primeiras linhas , as linhas que 
não contem o diretorio e a quelas linhas que não contem dados relevatens 
5.4 --> na linha [[if (exp[3] != "Name" and exp[3] != "----" and exp[0] != "da----" and exp[0] != "d-----"):]] eu 
estou excluindo nomes de diretorios e dados não nomeados trago pela função anterior
5.5 --> mesmo assim ainda temos um problema, muitos nomes de arquivos vem com espaço no meio, e como tivemos que 
utilizar varias vezes a função split para tratar os dados agora esses nomes estão separado, logo teremos que uni-los 
novamente, e é isso que fazemos nas linha seguintes 
5.6 --> antes de acabar a função salvamos os dados em um csv que iremos utilizar posteriormente, fazemos isso usando o 
pandas
 
'''


def escreva1(texto1):
    with open(r'C:\Users\ifrtef\Desktop\teste_de_escrita.txt', 'r+') as file:

        var = str(texto1)

        texto = var.split(r"\n")

        diretorio = []
        data = []
        hora = []
        name_file = []

        for i, line in enumerate(texto):
            exp = line.split(None)

            try:
                exp.index("Diret\\xa2rio:")
                var1 = " ".join(exp)
                var2 = var1[14:(len(var1) - 2)]
                var3 = var2.replace("\\\\", "\\")
                ver_fal = False

            except:
                ver_fal = True
                pass

            if (ver_fal and i > 5 and len(exp) > 4):
                if (exp[3] != "Name" and exp[3] != "----" and exp[0] != "da----" and exp[0] != "d-----"):
                    diretorio.append(var3)
                    data.append(exp[1])
                    hora.append(exp[2])
                    name_file.append(exp[4:-1])

        nome_final = []
        for line in name_file:
            var4 = " ".join(line)
            nome_final.append(var4)

        dicionario = {'diretorio': diretorio, 'data': data, 'hora': hora, 'name_arquivo': nome_final}

        df = pd.DataFrame(dicionario)
        df.to_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita.csv", sep=";")

    return df


def escreva2(texto2):
    with open(r'C:\Users\ifrtef\Desktop\teste_de_escrita2.txt', 'r+') as file:

        var = str(texto2)

        texto = var.split(r"\n")

        diretorio = []
        data = []
        hora = []
        name_file = []

        for i, line in enumerate(texto):
            exp = line.split(None)

            try:
                exp.index("Diret\\xa2rio:")
                var1 = " ".join(exp)
                var2 = var1[14:(len(var1) - 2)]
                var3 = var2.replace("\\\\", "\\")
                ver_fal = False

            except:
                ver_fal = True
                pass

            if (ver_fal and i > 5 and len(exp) > 4):
                if (exp[3] != "Name" and exp[3] != "----" and exp[0] != "da----" and exp[0] != "d-----"):
                    diretorio.append(var3)
                    data.append(exp[1])
                    hora.append(exp[2])
                    name_file.append(exp[4:-1])

        nome_final = []
        for line in name_file:
            var4 = " ".join(line)
            nome_final.append(var4)

        dicionario = {'diretorio': diretorio, 'data': data, 'hora': hora, 'name_arquivo': nome_final}

        df = pd.DataFrame(dicionario)
        df.to_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita2.csv", sep=";")

    return df


'''
mesma coisa do tranferencia mas aqui estou solicitando um novo processo o 
    Get-ChildItem -Path *caminho* -Force -Recurse" --> que força a leitura de cada arquivo nas pastas do diretorio 
'''


def worker1(rotina10):
    completed = subprocess.run(["powershell", "-Command", rotina10], capture_output=True)
    # print(completed)
    escreva1(completed)


def worker2(rotina20):
    completed = subprocess.run(["powershell", "-Command", rotina20], capture_output=True)
    # print(completed)
    escreva2(completed)


'''
escrever sobre os worker 110/200/300/400
'''


def worker100(rotina100):
    for k in range(1, (len(rotina100) + 1)):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim1"
        caminho_origem = fr"{rotina100['diretorio'][k]}\{rotina100['name_arquivo'][k]}"
        caminho_destino = fr"{caminho_dir_copia}\{caminho_origem[50:]}"
        rotina = f'Copy-Item -Path "{caminho_origem}" -Destination "{caminho_destino}" -Recurse -Force -Passthru'
        print(rotina)

        pasta_origem_arq = rotina100['diretorio'][k]

        c = '\\'
        pastas = []
        for pos, char in enumerate(pasta_origem_arq):
            if (char == c):
                pastas.append(pos)
        pastas.append(len(pasta_origem_arq))

        num_subpastas = len(pastas)

        testar_caminho_pasta_destino = os.access(fr"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:]}", os.F_OK)

        if testar_caminho_pasta_destino:
            transferencia100(rotina)


        else:
            for i in range(7, num_subpastas):

                if (os.access(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}", os.F_OK)):
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")



                else:
                    os.mkdir(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}")
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")

            transferencia100(rotina)


def worker200(rotina200):
    for k in range(1, (len(rotina200) + 1)):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim1"
        caminho_origem = fr"{rotina200['diretorio'][k]}\{rotina200['name_arquivo'][k]}"
        caminho_destino = fr"{caminho_dir_copia}\{caminho_origem[50:]}"
        rotina = f'Copy-Item -Path "{caminho_origem}" -Destination "{caminho_destino}" -Recurse -Force -Passthru'
        print(rotina)

        pasta_origem_arq = rotina200['diretorio'][k]

        c = '\\'
        pastas = []
        for pos, char in enumerate(pasta_origem_arq):
            if (char == c):
                pastas.append(pos)
        pastas.append(len(pasta_origem_arq))

        num_subpastas = len(pastas)

        testar_caminho_pasta_destino = os.access(fr"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:]}", os.F_OK)

        if testar_caminho_pasta_destino:
            transferencia200(rotina)


        else:
            for i in range(7, num_subpastas):

                if (os.access(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}", os.F_OK)):
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")



                else:
                    os.mkdir(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}")
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")

            transferencia200(rotina)


def worker300(rotina300):
    for k in range(1, (len(rotina300) + 1)):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim1"
        caminho_origem = fr"{rotina300['diretorio'][k]}\{rotina300['name_arquivo'][k]}"
        caminho_destino = fr"{caminho_dir_copia}\{caminho_origem[50:]}"
        rotina = f'Copy-Item -Path "{caminho_origem}" -Destination "{caminho_destino}" -Recurse -Force -Passthru'
        print(rotina)

        pasta_origem_arq = rotina300['diretorio'][k]

        c = '\\'
        pastas = []
        for pos, char in enumerate(pasta_origem_arq):
            if (char == c):
                pastas.append(pos)
        pastas.append(len(pasta_origem_arq))

        num_subpastas = len(pastas)

        testar_caminho_pasta_destino = os.access(fr"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:]}", os.F_OK)

        if testar_caminho_pasta_destino:
            transferencia300(rotina)


        else:
            for i in range(7, num_subpastas):

                if (os.access(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}", os.F_OK)):
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")



                else:
                    os.mkdir(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}")
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")

            transferencia300(rotina)


def worker400(rotina400):
    for k in range(1, (len(rotina400) + 1)):

        caminho_dir_copia = r"C:\Users\ifrtef\Desktop\scim1"
        caminho_origem = fr"{rotina400['diretorio'][k]}\{rotina400['name_arquivo'][k]}"
        caminho_destino = fr"{caminho_dir_copia}\{caminho_origem[50:]}"
        rotina = f'Copy-Item -Path "{caminho_origem}" -Destination "{caminho_destino}" -Recurse -Force -Passthru'
        print(rotina)

        pasta_origem_arq = rotina400['diretorio'][k]

        c = '\\'
        pastas = []
        for pos, char in enumerate(pasta_origem_arq):
            if (char == c):
                pastas.append(pos)
        pastas.append(len(pasta_origem_arq))

        num_subpastas = len(pastas)

        testar_caminho_pasta_destino = os.access(fr"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:]}", os.F_OK)

        if testar_caminho_pasta_destino:
            transferencia400(rotina)


        else:
            for i in range(7, num_subpastas):

                if (os.access(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}", os.F_OK)):
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")



                else:
                    os.mkdir(rf"{caminho_dir_copia}{pasta_origem_arq[pastas[7]:pastas[i]]}")
                    print(fr"{pasta_origem_arq[pastas[7]:pastas[i]]}")

            transferencia400(rotina)


if __name__ == "__main__":
    print("START")

    p1 = multiprocessing.Process(target=worker1, args=(rotina10,))
    p2 = multiprocessing.Process(target=worker2, args=(rotina20,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.close()
    p2.close()

    print('finish   p1 p2')

    df_db1 = pd.read_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita.csv", delimiter=";")

    meio1 = len(df_db1) // 2

    rotina100 = df_db1.iloc[1:meio1, :]
    rotina200 = df_db1.iloc[meio1:, :].reset_index(drop=True)

    df_db2 = pd.read_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita2.csv", delimiter=";")

    meio2 = len(df_db2) // 2

    rotina300 = df_db2.iloc[1:meio2, :]
    rotina400 = df_db2.iloc[meio2:, :].reset_index(drop=True)

    p10 = multiprocessing.Process(target=worker100, args=(rotina100,))
    p20 = multiprocessing.Process(target=worker200, args=(rotina200,))
    p30 = multiprocessing.Process(target=worker300, args=(rotina300,))
    p40 = multiprocessing.Process(target=worker400, args=(rotina400,))

    p10.start()
    p20.start()
    p30.start()
    p40.start()

    p10.join()
    p20.join()
    p30.join()
    p40.join()

    p10.close()
    p20.close()
    p30.close()
    p40.close()

    print(time.time() - tempo00)
