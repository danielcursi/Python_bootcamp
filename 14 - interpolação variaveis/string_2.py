nome = "Daniel"
idade = 24
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Daniel", "idade": 24}

print("Nome: %s Idade: %d" % (nome, idade)) # s string, d inteiro
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {0} Idade: {1} nome: {0} {0}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {age} {nome} {nome}".format(nome=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"nome: {nome} idade: {idade}")