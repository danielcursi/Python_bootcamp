nome = "DaNieL"

print(nome.upper()) # maiusculo
print(nome.lower()) # minusculo
print(nome.title()) # primeiro maiusculo

texto = "  Olá, mundo!    "

print(texto + ".")
print(texto.strip() + ".") # tira todos espaços
print(texto.rstrip() + ".") # tira espaço da direita
print(texto.lstrip() + ".") # tira espaço da esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#")) # 14 strings no total completando com => #
print("P-y-t-h-o-n")
print("-".join(menu)) # p-y-t-h-o-n