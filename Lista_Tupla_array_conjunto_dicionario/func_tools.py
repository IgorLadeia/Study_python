from functools import total_ordering

"""
muitas vezes queremos usar a orientação a objeto, mas devemos lembrar que essa extrutura não carrega com sigo 
alguns paradigmas da programação funcional. 

por exemplo quando fazemos a compração entre dois objetos o Python ira comprar o seu endereço de memoria e não seu 
conteuto tanto porque dentro de um objeto pode ter varios valores de comparação 

para essas operações de compração o python roda por traz asfunções (__lt__(), __le__(), __gt__()ou __ge__() __eq__) que
fazem a comparação 

então para fazermos a comparação de dois objetos é necessário a sobreescrita desses metodos. Melhor ainda o ppython ja 
desponibila uma functool onde voce só precisa criar as funções __eq__ e __lt__ e ele com essas duas faz todas as outras 
comprações 
"""

"""
MAS O QUE É UMA FUNCTOOL ?
O functoolsmódulo é para funções de ordem superior: funções que agem ou retornam outras funções. Em geral, 
qualquer objeto que pode ser chamado pode ser tratado como uma função para os propósitos deste módulo.
"""

"""
OBS : como as listas são mutaveis usamos sempre o self._name tornando uma lista de objetos privados. se quisermos 
modifica-la precisaremos criar suas funções setter e getter 

"""
@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo

        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme <= conta_da_daniela)

print(conta_do_guilherme <= conta_do_paulo)

print(conta_do_guilherme < conta_do_guilherme)

print(conta_do_guilherme == conta_do_guilherme)

print(conta_do_guilherme <= conta_do_guilherme)