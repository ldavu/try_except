try:
    nota1 = int(input("Qual a primeira nota? "))
    nota2 = int(input("Qual a segunda nota? "))
    qtdd_notas = int(input("Quantas notas vc digitou?"))
    media = (nota1 + nota2) / qtdd_notas
    print("Sua média é:", media)
except ValueError:
    print("Valores inválidos")
except ZeroDivisionError:
    print("Não pode dividir por zero")
except:
    print("Um erro estranho aconteceu.")
else:
    print("Média calculada com sucesso.")
finally:
    print("Bjo e até segunda")
    