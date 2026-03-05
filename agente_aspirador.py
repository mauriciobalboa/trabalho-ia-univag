import random

class Ambiente:
    def __init__(self):
        # Grade 2x2 (0 = limpo, 1 = sujo)
        self.grade = [[random.randint(0,1) for _ in range(2)] for _ in range(2)]
        self.posicao_agente = [0,0]

    def perceber(self):
        x, y = self.posicao_agente
        return {
            'posicao': (x, y),
            'sujo': self.grade[x][y] == 1
        }

    def executar(self, acao):
        x, y = self.posicao_agente

        if acao == "ASPIRAR":
            self.grade[x][y] = 0
            print("Aspirou a sujeira em", (x,y))

        elif acao == "DIREITA" and y < 1:
            self.posicao_agente[1] += 1

        elif acao == "BAIXO" and x < 1:
            self.posicao_agente[0] += 1

        elif acao == "ESQUERDA" and y > 0:
            self.posicao_agente[1] -= 1

        elif acao == "CIMA" and x > 0:
            self.posicao_agente[0] -= 1


class AgenteAspirador:
    def decidir(self, percepcao):
        if percepcao['sujo']:
            return "ASPIRAR"
        else:
            # movimento simples aleatório
            movimentos = ["CIMA", "BAIXO", "ESQUERDA", "DIREITA"]
            return random.choice(movimentos)


# execução do programa
ambiente = Ambiente()
agente = AgenteAspirador()

for i in range(10):
    percepcao = ambiente.perceber()
    acao = agente.decidir(percepcao)
    print("Percepção:", percepcao)
    print("Ação:", acao)
    ambiente.executar(acao)
    print("Posição atual:", ambiente.posicao_agente)
    print("Ambiente:", ambiente.grade)
    print()
