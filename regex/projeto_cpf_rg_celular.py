"""
1 - identificar os padroes de cadastro
2 - identificar os padroes individuais (rg - cpf -celular)
3 - criar uma classe que direciona o cadastro da informação
4 - criar função de cpf
5 - criar função de rg
6 - criar função de celular
"""
"""
----Cpf------
000.000.000-00
000111222-33
000 000 000 00

----rg-----
00.000.000-0
00 000 000 0
000000000

---celular----

(11)90000-0000
90000-0000
11900000000
900000000

"""
"""
----Cpf------
000.000.000-00
000111222-33
000 000 000 00

----rg-----
00.000.000-0
00 000 000 0
000000000

---celular----

(11)90000-0000
90000-0000
11900000000
900000000

"""
import re


class CadastroInicial:

    def __init__(self, name, identificador):
        self._name = name
        self._ident = self.descrobrir_modelo(identificador)

    def descrobrir_modelo(self, identificador):
        item = identificador.replace(" ","")
        cpf = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[.]?[-]?[0-9]{2}')
        rg = re.compile('[0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[.]?[-]?[0-9]')
        celular = re.compile('([(][0-9][0-9][)])?9[0-9]{4}[-]?[0-9]{4}')

        if len(item) <= 9:
            print("Nome: ",self._name, "RG: ",item)
        elif celular.match(item):
            print("Nome: ", self._name, "Celular: ", item)
        elif cpf.match(item):
            print("Nome: ", self._name, "CPF: ", item)
        else:
            print("cadastro errado")
        return ''


igor = CadastroInicial('igor ladeia',"95355-3428")
