temperatura = float(input("Digite uma temperatura atual: "))
if temperatura > 40.1:
    print("Você está com frebre")
elif temperatura <= 40.1 and temperatura >= 38.8:
    print("Você está com febrícula")
elif temperatura <= 38.8 and temperatura >= 37.0:
    print("Temperatura quase ideal")
elif temperatura <= 36.9 and temperatura >= 34.9:
    print("Temperatura normal")
elif temperatura <= 34.8 and temperatura >= 32.9:
    print("pre hipotermia")
elif temperatura <= 32.8 and temperatura >= 29.9:
    print("hiportemia")
else:
    print("R.I.P")