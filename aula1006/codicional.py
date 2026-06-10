# numero = 0
# if numero == 0:
#     print("O numero é zero")
# elif numero % 2 == 0:
#     print(f"O número {numero} é par")
# else:
#     print(f"O número {numero} é impar")


# while True:
#     idade = int(input("Digite a idade: "))

#     if idade >= 18:
#         print("Adulto")
#     elif idade < 18 and idade >= 12:
#         print("Adolecente")
#     else:
#         print("Crianca")
    
#     if idade == 0:
#         break


while True:
    nota = float(input("Digite uma nota: "))

    if nota > 90:
        print("Conceito A")
    elif nota >= 71 and nota <= 90:
        print("Conceito B")
    elif nota >= 61 and nota <= 70:
        print("Conceito C")
    elif nota >= 49 and nota <= 60:
        print("Conceito D")
    else:
        print("Conceito E")
    
    if nota == -1:
        print("Saindo do Sistema")
        break
