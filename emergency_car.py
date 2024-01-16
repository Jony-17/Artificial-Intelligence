import asyncio
import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from color import BLACK, RED, BLUE, GREEN, GREY, WHITE, YELLOW

class EmergencyCar(Agent):
    def __init__(self, jid, password, environment, posicaox, posicaoy, sentido_carro):
        super().__init__(jid, password)
        self.environment = environment
        self.posicao_carro_X = posicaox
        self.posicao_carro_Y = posicaoy
        self.sentido_carro = sentido_carro
        self.velocidade = 1
        self.faixa = "Desconhecida"
        self.faixa_sentido = "Desconhecido"
        self.estado_da_faixa = RED
        self.status = True

    async def setup(self):
        print("Agente carro de emergência começou")

        class EmergencyCarBehaviour(CyclicBehaviour):
            async def run(self):
                #print(f"Carro de emergencia a funcionar: {self.agent.jid}")

                self.agent.faixa = self.agent.environment.obter_estado_semaforo(self.agent.posicao_carro_X, self.agent.posicao_carro_Y, self.agent.status, self.agent.sentido_carro)

                if self.agent.faixa=="Saiu da cidade":
                    #print(f"{self.agent.jid} -> Saiu da cidade")
                    #self.kill()
                    if self.agent.sentido_carro == "O":
                        self.agent.posicao_carro_X += 456

                    elif self.agent.sentido_carro == "E":
                        self.agent.posicao_carro_X -= 456

                    elif self.agent.sentido_carro == "N":
                        self.agent.posicao_carro_Y += 456

                    elif self.agent.sentido_carro == "S":
                        self.agent.posicao_carro_Y -= 456

                    else:
                        self.kill()

                elif self.agent.faixa=="Mantem parado que ainda está vermelho":
                    self.agent.estado_da_faixa = RED
                    self.agent.status = False
                    
                elif self.agent.faixa=="Direita" or self.agent.faixa=="Esquerda":
                    #print("O carro pode virar ")
                    resultado = random.choice([True, False])  # Gera aleatoriamente se o carro vai virar: "sim" ou "não"
                    #print(f"Valor random: {resultado}")

                    if resultado == True and self.agent.faixa == "Direita":
                        #print("O carro muda de direção para a direita!")
                        self.agent.velocidade = 7

                        if self.agent.sentido_carro == "E":
                            self.agent.sentido_carro = "S"
                            self.agent.posicao_carro_Y += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "S":
                            self.agent.sentido_carro = "O"
                            self.agent.posicao_carro_X -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        elif self.agent.sentido_carro == "O":
                            self.agent.sentido_carro = "N"
                            self.agent.posicao_carro_Y -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        elif self.agent.sentido_carro == "N":
                            self.agent.sentido_carro = "E"
                            self.agent.posicao_carro_X += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                    
                    elif resultado == True and self.agent.faixa == "Esquerda":
                        #print("O carro muda de direção para a esquerda!")

                        if self.agent.sentido_carro == "E":
                            self.agent.sentido_carro = "N"
                            self.agent.posicao_carro_Y -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "S":
                            self.agent.sentido_carro = "E"
                            self.agent.posicao_carro_X += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "O":
                            self.agent.sentido_carro = "S"
                            self.agent.posicao_carro_Y += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "N":
                            self.agent.sentido_carro = "O"
                            self.agent.posicao_carro_X -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                    else:
                        self.agent.status = True
                        self.agent.estado_da_faixa = GREEN
                        if self.agent.sentido_carro == "E":
                            self.agent.posicao_carro_X += self.agent.velocidade

                        elif self.agent.sentido_carro == "O":
                            self.agent.posicao_carro_X -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "N":
                            self.agent.posicao_carro_Y -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                        elif self.agent.sentido_carro == "S":
                            self.agent.posicao_carro_Y += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                    self.agent.velocidade = 1

                elif self.agent.faixa == -1: # Se for VERDE
                    self.agent.status = True
                    self.agent.estado_da_faixa = GREEN
                    if self.agent.sentido_carro == "E":
                        self.agent.posicao_carro_X += self.agent.velocidade
                        #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                    elif self.agent.sentido_carro == "O":
                        self.agent.posicao_carro_X -= self.agent.velocidade
                        #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                    elif self.agent.sentido_carro == "N":
                        self.agent.posicao_carro_Y -= self.agent.velocidade
                        #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                    elif self.agent.sentido_carro == "S":
                        self.agent.posicao_carro_Y += self.agent.velocidade
                        #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")

                else: # Se for VERMELHO recebe posição de parada
                    self.agent.estado_da_faixa = RED
                    #print("O carro  recebeu posição de parada")

                    if self.agent.sentido_carro == "E":
                        if (self.agent.posicao_carro_X+self.agent.velocidade) < self.agent.faixa:
                            self.agent.status = True
                            self.agent.posicao_carro_X += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        else:
                            self.agent.status = False
                            #print("Carro parou porque está vermelho")

                    elif self.agent.sentido_carro == "O":
                        if (self.agent.posicao_carro_X-self.agent.velocidade) > self.agent.faixa:
                            self.agent.status = True
                            self.agent.posicao_carro_X -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        else:
                            self.agent.status = False
                            #print("Carro parou porque está vermelho")

                    elif self.agent.sentido_carro == "N":
                        if (self.agent.posicao_carro_Y-self.agent.velocidade) > self.agent.faixa:
                            self.agent.status = True
                            self.agent.posicao_carro_Y -= self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        else:
                            self.agent.status = False
                            #print("Carro parou porque está vermelho")

                    elif self.agent.sentido_carro == "S":
                        if (self.agent.posicao_carro_Y+self.agent.velocidade) < self.agent.faixa:
                            self.agent.status = True
                            self.agent.posicao_carro_Y += self.agent.velocidade
                            #print(f"O {self.agent.jid} avançou para: [{self.agent.posicao_carro_X};{self.agent.posicao_carro_Y}]")
                        else:
                            self.agent.status = False
                            #print("Carro de emergencia parou porque está vermelho")

                self.agent.environment.createEmergencyCar(self.agent.jid, self.agent.posicao_carro_X, self.agent.posicao_carro_Y, self.agent.sentido_carro, self.agent.status)
                await asyncio.sleep(0.1)
        self.add_behaviour(EmergencyCarBehaviour())