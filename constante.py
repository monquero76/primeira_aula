# DESCONTO = 10
# preco = 100
# print(preco * (100 - DESCONTO)/100)

# PI = 3.14
# PI = 3.15

# print(PI)

#Criar uma variavel para a maquina injetora de plastico H-400
nomeInjetora = "Injetora de plástico H-400"
#Criar uma variavel para a quandiade de ciclos por segundo
totalCliclos = 5820
#Criar uma variavel para a temperatura da zona 01
tempZ01 = 210.5
#Criar uma constante para valor de temperatura máxima
TEMPERATURAMAXIMA = 250.0
#Criar uma varival para saber se o sensor esta ativo TRUE
sensorSegurancaAtivo = True


texto = f"""
Nome da Injetora        {nomeInjetora}
Cliclos por Segundo     {totalCliclos}
Temperatura Zona01      {tempZ01}
Temperatura Máxima      {TEMPERATURAMAXIMA}
Sensor Ativo            {sensorSegurancaAtivo}
"""

print(texto)