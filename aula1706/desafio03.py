#Cria uma lista com 10 elementos, usando string e numeros.
mista = ["Maria", 16, "Marcio", 40, "Antonio", 23, "Vitor", 20, "Douglas", 50]
#Mostrar a lista com for
for i in mista:
    print(f"{i}")
#Inserir 3 elementos com append e mais 3 com insert(indice 0, 4, 10)
mista.append("Katia")
mista.append(48)
mista.append("Lucas")
mista.insert(0, "José")
mista.insert(4, 100)
mista.insert(10, "Fim")   
print(f"Lista apos acrescimos {mista}")

#Editar um elemento no indice 3 (tirar um colocar outro no lugar)
    
#Excluir o elemento do indice 14 usando valor(remove)
    
#Ecluir o elemento de indice 7 usando pop

#Excluir o elemento de indice 1 usando del
    
#Mostarr se o elemento "Computador" existe na lista
    
#Descobrir a posição de uma elemento usando index
indice = mista.index("Douglas")
print(indice)

#Percorrer a lista mostrando indice e valor
for i, elemento in enumerate(mista):
    print(f"{i+1} - {elemento}")
#Limpar toda a lista
mista.clear()
print(f"{mista} - lista foi limpa")
