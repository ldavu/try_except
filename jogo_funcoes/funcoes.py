import random

def sortearBatalha():
    locaisBatalhas = ["Floresta Malígna","Pântano Gosmento", "Caverna Sombria", "Lago Repugnante", "Deserto Escaldante"]
    inimigosBatalhas = ["Aranha Zumbi", "Verme Gigante", "Ciclope Rastejante","Ogro Impetuoso", "Medusa Feiticeira"]

    local = random.choice(locaisBatalhas)
    monstro = random.choice(inimigosBatalhas)
    print(f"Seu caminho lhe trouxe a um local perigoso: {local}. Nesse local, uma terrível ameaça se apresenta: {monstro}")    

def realizarBatalha():
    destino = random.randint(0,1)
    if destino == 0:
        print("Você venceu! Ganhou mais um ponto.")
        return 1
    else:
        print("Você sofreu uma derrota! Perdeu um ponto.")
        return -1  
    
def lampada(parEscolha):
    if parEscolha == "Sim":
        destino = random.randint(0,1)
        if destino == 0:
            print("Você recebeu a benção dos pontos positivos. Ganhou 5 pontos.")
            return 5
        else:
            print("Você despertou a maldição dos pontos negativos. Perdeu 5 pontos.")
            return -5
    else: 
        print("Quem sabe na próxima...")    
