from io import UnsupportedOperation
import random, funcoes

from idna import valid_contextj

jogadores = []

nome = input("Nome de jogador/jogadora 1: ")
jogadores.append(nome)
nome = input("Nome de jogador/jogadora 2: ")
jogadores.append(nome)

progresso = [0,0]
pontos = [0,0]

mensagemBatalhas = ["Você venceu! Ganhou mais um ponto.", "Você sofreu uma derrota! Perdeu 1 ponto."]
vez = 0
dado = 0
proximaRodada = True

while proximaRodada:
    print(f"\nSua vez, {jogadores[vez]}!")
    input("Pressione ENTER para jogar o dado:")
    dado = random.randint(1,3)
    progresso[vez] += dado
    print(f"Você tirou {dado}, e foi até a posição {progresso[vez]}")
    input("Pressione Enter")

    if progresso[vez] == 1:
        funcoes.sortearBatalha()
        pontos[vez] += funcoes.realizarBatalha()

    elif progresso[vez] == 2:
        print("Você encontrou um diamante e ganhou 5 pontos.") 
        pontos[vez] += 5
    elif progresso[vez] == 3:
        funcoes.sortearBatalha()
        pontos[vez] += funcoes.realizarBatalha()

    elif progresso[vez] == 4:
        try:
            escolha = input("Há dois caminhos, esquerda e direita. Qual vai pegar?")
            destino = random.randint(0,1)
            if destino == 0:
                print("Boa escolha, caminho tranquilo. Ganhou 1 ponto.")
                pontos[vez] += 1
            else:
                print("Péssima escolha, caminho cheio de insetos. Perdeu 1 ponto.")
                pontos[vez] -= 1
        except ValueError:
            print("Não pode colocar inteiros!")
        except:
            print("Valor desconhecido!")
        else:
            pass

    elif progresso[vez] == 5:
        funcoes.sortearBatalha()
        pontos[vez] += funcoes.realizarBatalha()

    elif progresso[vez] == 6:
        print("Você encontrou uma runa mágica e ganhou 10 pontos.") 
        pontos[vez] += 10            
    
    elif progresso[vez] == 7:
        
        try:
            print(jogadores[vez], "você encontrou uma lâmpada mágica. Esfregue-a para saber o que vai receber.") 
            escolha = input("Vai esfregar a lâmpada? Sim ou Não")
            pontos[vez] += funcoes.lampada(escolha)
        except ValueError:
            print("Não pode ser Numeros")
        else:
            pass


    elif progresso[vez] >= 8:
        print(f"Parabéns {jogadores[vez]}, você ganhou! Sua pontuação foi de: {pontos[vez]}")            
        proximaRodada = False

    print(f"{jogadores[vez]}, você está com {pontos[vez]} pontos.")
    input("Pressione Enter")
    if vez == 0:
        vez = 1
    else:
        vez = 0

