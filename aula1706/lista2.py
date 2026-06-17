#Crie uma lista de compras
#Adicione 2 elementos
#Substitua os elementos de indices 3 e 5

compras = ["cafe", "pão", "mussarela", "leite"]
# indice = 0;
# for c in compras:
#     indice +=1
#     print(f"{indice} - {c}")

compras.append("carne")
compras.append("sabão")

print(compras)

compras[3] = "presunto"
compras[5] = "frango"

for c in range(len(compras)):
    print(f"{c+1} - {compras[c]}")