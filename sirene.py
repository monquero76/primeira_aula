import winsound
import time

print("-------------------------------")
print("Perigo: Célula em Inicialização")
print("-------------------------------")
print("Ligando Exaustor de Gases...")
time.sleep(1)

print("Energizando Braço Robótico...")
time.sleep(1)

print("Aguardando Comando de Start do Operador")

for _ in range(5):
    winsound.Beep(800, 300)
    winsound.Beep(1200, 300)

print("Sistema Pronto para Operação")