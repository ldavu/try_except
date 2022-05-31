from audioop import avg
from multiprocessing.sharedctypes import Value
import random

def mostrarMenu():
    try:
        print("\nDigite o número da opção desejada:")
        print("1. Fazer leitura das velocidades")
        print("2. Mostrar todos os registros")
        print("3. Mostrar acima do limite")
        print("4. Mostrar média das velocidades")
        print("5. Mostrar a maior velocidade registrada")
        print("6. Sair do programa")
        
        opcao = int(input("Opção: "))
    except ValueError:
        print("Valor invalido!")
    else:
        pass
    finally:
        return opcao



    #return int(input("Opção: "))

def fazerLeitura():
    velocidades = []
    quantidade = int(input("Quantas velocidades serão lidas? "))
    
    for carro in range(quantidade):
        leitura = random.randint(1,150)
        velocidades.append(leitura)

    print("Leituras realizadas com sucesso.")
    return velocidades

def mostrarTodos(parLista):
    indice = 1
    for item in parLista:
        print(f"{indice} - {item}")
        indice += 1

def mostrarAcima(parLista, parLimite):
    indice = 1
    for item in parLista:
        
        if item > parLimite:
            print(f"{indice} - {item}")
        
        indice += 1
        
def mostrarMedia(parLista):
    # soma = 0
    # for item in parLista:
    #     soma =+ item

    soma = sum(parLista)
    quantidade = len(parLista)
    media = soma / quantidade

    return media

def mostrarMaior(parLista): 
    maior = 0
    for item in parLista:
        if item > maior:
            maior = item

    # maior = max(parLista)
    print(f"A maior velocidade registrada foi: {maior}")
