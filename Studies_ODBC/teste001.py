

import pyodbc
import pandas as pd

class ConectarDB:
    def __init__(self):
        # Criando conexão.'
        self.con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\LUTTER\FA_2018_08_08_V9a.mde;')
        # Criando cursor.
        self.cur = self.con.cursor()

    def exibir_tabelas(self):
        nomes = []
        for tabela in self.cur.tables(tableType='TABLE'):
            # print(tabela.table_name)
            nomes.append(tabela.table_name)
        return nomes

    def consultar_nome_coluna(self,tabela):
        return self.cur.columns(table=f'{tabela}')

    def consultar_tudo(self,tabela):
        return self.cur.execute(F"SELECT * FROM {tabela}").fetchall()

    def insert (self,cursor):
        self.cur.execute("INSERT INTO Check VALUES (?,?,?,?)", cursor)

    def header(self,tabela):
        return self.cur.execute(f'EXEC {tabela}').fetchall()



if __name__ == '__main__':
    banco = ConectarDB()
    tabelass = banco.exibir_tabelas()

    print("------------------------------------------")

    db = []
    for table in tabelass:
        db.append(f"{table}")
        teste = banco.consultar_nome_coluna(f"{table}")
        for row in teste:
            db.append(row)
        print("------------------------------------------")

    df = pd.DataFrame(db)
    df.to_csv(r"C:\Users\ifrtef\Desktop\db.csv", sep=",")




    # gosto = (
    #     25,'MAXxx',20201,'SCANIA TESTE001'
    # )
    #
    # # banco.insert(gosto)
    # ok = banco.header("tmp_213_TQ_TopABC1")
    # print(ok)
    #
    #
    #
    # PELO_AMOR_DE_DEUS = banco.consultar_nome_coluna("tmp_AnlaufPhasenPaar_VB")
    # for row in PELO_AMOR_DE_DEUS:
    #     print(row.column_name)
    #




    #
    # teste = banco.consultar_tudo("Beanstandungen")
    # cont = []
    # for row in teste:
    #     cont.append(row)
    #     print(row)
    #



    # for row in cursor.columns(table='x'):
    #     print(row.column_name)