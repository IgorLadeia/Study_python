import subprocess
import pandas as pd
import os


df_db1 = pd.read_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita.csv", delimiter=";")

meio1 = len(df_db1) // 2


rotina100 = df_db1.iloc[1:meio1, :]
rotina200 = df_db1.iloc[meio1:, :].reset_index(drop = True)




df_db2 = pd.read_csv(r"C:\Users\ifrtef\Desktop\teste_de_escrita2.csv", delimiter=";")

meio2 = len(df_db2) // 2

rotina300 = df_db1.iloc[1:meio1, :]
rotina400 = df_db1.iloc[meio2:, :]

print(rotina200)
    #
    # for line in range(meio1,len(rotina200)):
    #     print(line)
