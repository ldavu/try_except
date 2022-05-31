from ctypes import resize
import radar_funcoes

registros = []
limite = int(input("Qual o limite de velocidade?"))
escolha = radar_funcoes.mostrarMenu()

while escolha != 6:
    if escolha == 1:
        registros = radar_funcoes.fazerLeitura()
    elif escolha == 2:
        radar_funcoes.mostrarTodos(registros)
    elif escolha == 3:
        radar_funcoes.mostrarAcima(registros,limite)
    elif escolha == 4:
        resultado = radar_funcoes.mostrarMedia(registros)
        print("A média das velocidades registradas é",resultado)
    elif escolha == 5:
        radar_funcoes.mostrarMaior(registros)

    escolha = radar_funcoes.mostrarMenu()

print("Programa encerrado.")