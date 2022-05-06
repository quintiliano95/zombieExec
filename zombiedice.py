from random import randint, shuffle


class Dado:
    def __init__(self, cor, lados, ladoSorteado):
        self.cor = cor
        self.lados = lados
        self.ladoSorteado = ladoSorteado


class Jogador:
    def __init__(self, nome, cerebros, tiros):
        self.nome = nome
        self.cerebros = cerebros
        self.tiros = tiros


def SiglaParaAcao(argument):
    switcher = {
        "C": "Cerebro",
        "P": "Passo",
        "T": "Tiro",
    }
    return switcher.get(argument, "Sigla Não Implementada")


def Acao(dadoSorteado):
    for acao in dadoSorteado:
        print(tab, SiglaParaAcao(acao))


def VerificarGanhador(listaJogadores):
    for jogador in listaJogadores:
        if(jogador.cerebros >= 13):
            print('O jogador ', jogador.nome,  ' ganhou!')
            return True
        else:
            return False


def VerificarPerdedor(listaJogadores):
    for jogador in listaJogadores:
        if(jogador.tiros >= 3):
            print('O jogador ', jogador.nome,  ' perdeu!')
            listaJogadores.remove(jogador)
            return True
        else:
            return False


def JogaDado(listaDados):
    dado = listaDados.pop()
    numSorteado = randint(0, 5)
    dado.ladoSorteado = dado.lados[numSorteado]
    print(tab, dado.cor, ' ', SiglaParaAcao(dado.ladoSorteado))

    return dado


def StatusJogador(jogadorAtual):
    print(tab, jogadorAtual.nome)
    print(tab, tab, "Cerebros ", jogadorAtual.cerebros)
    print(tab, tab, "Tiros ", jogadorAtual.tiros)


def VerificaTipoLado(listaDadosJogados, jogadorAtual):
    for dado in listaDadosJogados:
        if(dado.ladoSorteado == "C"):
            jogadorAtual.cerebros = jogadorAtual.cerebros + 1
        elif(dado.ladoSorteado == "T"):
            jogadorAtual.tiros = jogadorAtual.tiros + 1


tab = '    '

print('ZOMBIE DICE!')
print('Seja bem-vindo ao jogo Zombie Dice!')

numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input('Informe a quantidade de jogadores: '))

    if (numJogadores < 2):
        print('AVISO: Você precisa de pelo menos 2 jogadores!\n')

listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    listaJogadores.append(Jogador(nome, 0, 0))


ladosDadoVerde = ["C", "P", "C", "T", "P", "C"]
ladosDadoAmarelo = ["T", "P", "C", "T", "P", "C"]
ladosDadoVermelho = ["T", "P", "T", "C", "P", "T"]
alguemGanhou = False

dadoVerde = Dado("Verde", ladosDadoVerde, "")
dadoAmarelo = Dado("Amarelo", ladosDadoAmarelo, "")
dadoVermelho = Dado("Vermelho", ladosDadoVermelho, "")

listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

listaDadosJogados = []

print('INICIANDO O JOGO...')
while(not alguemGanhou):
    for jogadorAtual in listaJogadores:  # Proxima rodada do jogo
        print('É a vez de', jogadorAtual.nome + '...')

        shuffle(listaDados)  # Embaralhar todos os dados da garrafa

        dado1 = JogaDado(listaDados)
        dado2 = JogaDado(listaDados)
        dado3 = JogaDado(listaDados)

        shuffle(listaDados)  # Embaralhar todos os dados da garrafa

        listaDadosJogados.clear()
        listaDadosJogados.append(dado1)
        listaDadosJogados.append(dado2)
        listaDadosJogados.append(dado3)

        VerificaTipoLado(listaDadosJogados, jogadorAtual)

        listaDados.append(dado1)
        listaDados.append(dado2)
        listaDados.append(dado3)

        shuffle(listaDados)  # Embaralhar todos os dados da garrafa

        StatusJogador(jogadorAtual)

        alguemGanhou = VerificarGanhador(listaJogadores)

        if(alguemGanhou):
            break

        perdeu = VerificarPerdedor(listaJogadores)

        if(len(listaJogadores) == 1):
            print('O jogador ', listaJogadores[0].nome, ' ganhou!!')
            alguemGanhou = True
            break

print('O jogo Terminou...')

input('Pressione Enter para sair!')