#Crie a lista
#Exclui elementos pelo valor(valor é o valor da string)

pecas = ["Retrovisor", "Volante", "Buzina", "Pedais", "Pastilhas de Freio", "Bomba de Água"]
# print(len(pecas))
print("=============================================================================================================")
print(f"lista original de pecas: {pecas}")
print("=============================================================================================================")
pecas.remove("Buzina") #remover pelo valor
print(f"Lista com remoção pelo valor: {pecas}")
print("========================================================================================================")
pecas.pop(0) #removendo valor pelo indice
print(f"Lista com remoção com pop e indice: {pecas}")
print("================================================================================================")
del pecas[1]
print(f"Lista com remoção del e indice: {pecas}")
print("==================================================================================")
