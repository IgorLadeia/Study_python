"""
Compreensão de listas é uma maneira simplificada de gerar listas
e sua sintax é bem siimples

[expressão for item in lista]

"""

lista = [item**2 for item in range(10)]
print(lista)

lista2 = ["igor", "ladeia" , "freitas"]
lista2 = [item.upper() for item in lista2 ]
print(lista2)


"""
Compreensão de listas com condicional 
[expr for item in lista if cond]
"""

resultado = [numero for numero in range(20) if numero % 2 == 0]
print(resultado)

"""
Compreensão de listas com varias condicional 
[expr for item in lista if cond]
"""

resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
print(resultado)

"""
Compreensão de listas com if e else
[expr for item in lista if cond]
"""

resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
print(resultado)