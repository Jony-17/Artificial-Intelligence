import asyncio
from environment import Environment
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from color import RED, GREEN

class TrafficLightAgent(Agent):
    def __init__(self, jid, password, environment, coordenadaX, coordenadaY, SentEY, SentEXMin, SentEXMax, SentOY, SentOXMin, SentOXMax, SentNX, SentNYMin, SentNYMax, SentSX, SentSYMin, SentSYMax):                                                            
        super().__init__(jid, password)
        self.environment = environment
        self.semaforo_estado = RED
        self.semafor_coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

        #Var's Sentido Este
        self.SentEY = SentEY
        self.SentEXMin = SentEXMin
        self.SentEXMax = SentEXMax

        #Var's Sentido Oeste
        self.SentOY = SentOY
        self.SentOXMin = SentOXMin
        self.SentOXMax = SentOXMax

        #Var's Sentido Norte
        self.SentNX = SentNX
        self.SentNYMin = SentNYMin
        self.SentNYMax = SentNYMax

        #Var's Sentido Sul
        self.SentSX = SentSX
        self.SentSYMin = SentSYMin
        self.SentSYMax = SentSYMax

        self.estadoN = RED
        self.estadoS = RED
        self.estadoE = RED
        self.estadoO = RED

        #Variáveis de métrica
        self.tempo_parado_NS = 0
        self.tempo_parado_EO = 0

        environment.createTrafficLight(jid, SentEY, SentEXMin, SentEXMax, SentOY, SentOXMin, SentOXMax, SentNX, SentNYMin, SentNYMax, SentSX, SentSYMin, SentSYMax, self.estadoN, self.estadoS, self.estadoO, self.estadoE)

    
    async def setup(self):
        print("Agente semáforo começou")
        
        template = Template()
        template.set_metadata("performative", "request")

        class TrafficLightBehaviour(CyclicBehaviour):
            async def run(self):
                contagemEmerNS, contagemEmerOE = self.agent.environment.contar_carros_emergencia(self.agent.jid)
                contagemNS, contagemOE = self.agent.environment.contar_carros(self.agent.jid)
                contagem_paradosNS, contagem_paradosOE = self.agent.environment.contar_carros_parados(self.agent.jid)
                
                if(contagemEmerNS > contagemEmerOE):
                    await asyncio.sleep(2)
                    self.agent.estadoO = self.agent.estadoE = RED
                    Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)
                    await asyncio.sleep(2.5)
                    self.agent.estadoN = self.agent.estadoS = GREEN
                    Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)
                elif(contagemEmerNS < contagemEmerOE):
                    await asyncio.sleep(2)
                    self.agent.estadoN = self.agent.estadoS = RED
                    Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)
                    await asyncio.sleep(2.5)
                    self.agent.estadoO = self.agent.estadoE = GREEN
                else:
                    if((contagemNS + contagem_paradosNS) > (contagemOE + contagem_paradosOE)):
                        await asyncio.sleep(2)
                        self.agent.estadoO = self.agent.estadoE = RED
                        Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)
                        await asyncio.sleep(2.5)
                        self.agent.estadoN = self.agent.estadoS = GREEN
                        Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)

                    elif((contagemNS + contagem_paradosNS) <= (contagemOE + contagem_paradosOE)):
                        await asyncio.sleep(2)
                        self.agent.estadoN = self.agent.estadoS = RED
                        Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)
                        await asyncio.sleep(2.5)
                        self.agent.estadoO = self.agent.estadoE = GREEN
                Environment.updateTrafficLight(self.agent.jid, self.agent.estadoN, self.agent.estadoS, self.agent.estadoO, self.agent.estadoE)

        self.add_behaviour(TrafficLightBehaviour())