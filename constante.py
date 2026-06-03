# DESCONTO = 10
# preco = 100
# print(preco * (100 - DESCONTO)/100)

# PI = 3.14
# PI = 3.15

# print(PI)

#Criar uma variavel para a maquina injetora de plastico H-400
nomeInjetora = "H-400"
#Criar uma variavel para a quandiade de ciclos por segundo
cps = 5820
#Criar uma variavel para a temperatura da zona 01
temp01 = 210.5
#Criar uma varival para saber se o sensor esta ativo TRUE
sAtivo = True

texto = f"""
Nome da Injetora        {nomeInjetora}
Cliclos por Segundo     {cps}
Temperatura Zona01      {temp01}
Sensor Ativo            {sAtivo}
"""

print(texto)