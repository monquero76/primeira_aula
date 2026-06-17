#Descobrindo o tamanho da lista
nomes = ["Jose", "Maria", "Antonio", "Marcio", "Vitor"]
print(len(nomes)) #exibe o tamanho da lista

if "Antonio" in nomes:
    print("Antonio Jeferson está ativo")
else:
    print("Antonio Jeferson matou aula")

#posicao de um elemento na lista
indice = nomes.index("Antonio")
print(f"{nomes[indice]} esta no indice: {indice}")
print(" ")

#Percorrer a lista
for n in range(len(nomes)):
    print(f"{n+1} - {nomes[n]}")
print(" ")

#Percorrer a lista com indice e valor com metodo Python - enumerate
for n, nome in enumerate(nomes):
    print(f"{n+1} - {nome}")

#Limpar toda a lista
nomes.clear()
print(nomes)