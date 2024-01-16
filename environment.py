from color import RED, GREEN, GREY, YELLOW
import pygame

trafficlight_dict = {
    "id": [],
    "SentEY": [],
    "SentEXMin": [],
    "SentEXMax": [],
    "SentOY": [],
    "SentOXMin": [],
    "SentOXMax": [],
    "SentNX": [],
    "SentNYMin": [],
    "SentNYMax": [],
    "SentSX": [],
    "SentSYMin": [],
    "SentSYMax": [],
    "estadoN": [],
    "estadoS": [],
    "estadoO": [],
    "estadoE": [],
    }

car_dict = {
    "id": [],
    "posx": [],
    "posy": [],
    "sentido": [],
    "status":[]
    }

emergency_car_dict = {
    "id": [],
    "posx": [],
    "posy": [],
    "sentido": [],
    "status":[]
    }

'''"lim_x1": [],
    "lim_x2": [],
    "lim_y1": [],
    "lim_y2": [],'''

respawn_dict = {
    "x": [0, 108],
    "y":[124, 0]
    }

class Environment:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()

        # Definir as dimensões da janela
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 456, 456

        # Coordenadas do centro da janela
        self.center_x = self.WINDOW_WIDTH // 2
        self.center_y = self.WINDOW_HEIGHT // 2

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Simulação de Tráfego")

        # Criação de background
        self.background = pygame.image.load('images/relva.png')

        # Criação semáforos vermelho e verde
        self.red = pygame.image.load('images/redN.png')
        self.red = pygame.transform.scale(self.red, (4, 12))

        self.green = pygame.image.load('images/greenN.png')
        self.green = pygame.transform.scale(self.green, (4, 12))

        # Criação semáforos vermelho Norte e verde Norte
        self.redN = pygame.image.load('images/redN.png')
        self.redN = pygame.transform.scale(self.redN, (4, 12))

        self.greenN = pygame.image.load('images/greenN.png')
        self.greenN = pygame.transform.scale(self.greenN, (4, 12))

        # Criação semáforos vermelho Sul e verde Sul
        self.redS = pygame.image.load('images/redS.png')
        self.redS = pygame.transform.scale(self.redS, (4, 12))

        self.greenS = pygame.image.load('images/greenS.png')
        self.greenS = pygame.transform.scale(self.greenS, (4, 12))

        # Criação semáforos vermelho Este e verde Este
        self.redE = pygame.image.load('images/redE.png')
        self.redE = pygame.transform.scale(self.redE, (12, 4))

        self.greenE = pygame.image.load('images/greenE.png')
        self.greenE = pygame.transform.scale(self.greenE, (12, 4))

        # Criação semáforos vermelho Oeste e verde Oeste
        self.redO = pygame.image.load('images/redO.png')
        self.redO = pygame.transform.scale(self.redO, (12, 4))

        self.greenO = pygame.image.load('images/greenO.png')
        self.greenO = pygame.transform.scale(self.greenO, (12, 4))

        # Criação carro virado para a direita
        self.car_right = pygame.image.load('images/car_right.png')
        self.car_right = pygame.transform.scale(self.car_right, (18, 6))

        # Criação carro virado para a esquerda
        self.car_left = pygame.image.load('images/car_left.png')
        self.car_left = pygame.transform.scale(self.car_left, (18, 6))

        # Criação carro virado para cima
        self.car_up = pygame.image.load('images/car_up.png')
        self.car_up = pygame.transform.scale(self.car_up, (6, 18))

        # Criação carro virado para baixo
        self.car_down = pygame.image.load('images/car_down.png')
        self.car_down = pygame.transform.scale(self.car_down, (6, 18))

        # Criação carro de emergência virado para a direita
        self.emegency_car_right = pygame.image.load('images/emegency_car_right.png')
        self.emegency_car_right = pygame.transform.scale(self.emegency_car_right, (18, 6))

        # Criação carro de emergência virado para a esquerda
        self.emegency_car_left = pygame.image.load('images/emegency_car_left.png')
        self.emegency_car_left = pygame.transform.scale(self.emegency_car_left, (18, 6))

        # Criação carro de emergência virado para cima
        self.emegency_car_up = pygame.image.load('images/emegency_car_up.png')
        self.emegency_car_up = pygame.transform.scale(self.emegency_car_up, (6, 18))

        # Criação carro de emergência virado para baixo
        self.emegency_car_down = pygame.image.load('images/emegency_car_down.png')
        self.emegency_car_down = pygame.transform.scale(self.emegency_car_down, (6, 18))

    def run(self):

        self.window.blit(self.background, (0, 0)) # Imagem da interseção
        pygame.display.update()

        # Linhas amarelas a separar sentidos
        pygame.draw.line(self.window, YELLOW, (0, 110), (456, 110), 2) #Linha amarela a separar sentidos
        pygame.draw.line(self.window, YELLOW, (0, 338), (456, 338), 2) #Linha amarela a separar sentidos
        pygame.draw.line(self.window, YELLOW, (110, 0), (110, 456), 2) #Linha amarela a separar sentidos
        pygame.draw.line(self.window, YELLOW, (338, 0), (338, 456), 2) #Linha amarela a separar sentidos


        # Ruas horizontais
        pygame.draw.line(self.window, GREY, (0, 102), (456, 102), 12)
        pygame.draw.line(self.window, GREY, (0, 118), (456, 118), 12)
        pygame.draw.line(self.window, GREY, (0, 330), (456, 330), 12)
        pygame.draw.line(self.window, GREY, (0, 346), (456, 346), 12)

        # Ruas verticais
        pygame.draw.line(self.window, GREY, (102, 0), (102, 456), 12)
        pygame.draw.line(self.window, GREY, (118, 0), (118, 456), 12)
        pygame.draw.line(self.window, GREY, (330, 0), (330, 456), 12)
        pygame.draw.line(self.window, GREY, (346, 0), (346, 456), 12)
        

        for i in range(len(trafficlight_dict["id"])):
            # Desenhar semáforos
            if trafficlight_dict["estadoE"][i] == RED:
                self.window.blit(self.redE, (trafficlight_dict["SentEXMax"][i]-16, trafficlight_dict["SentEY"][i]+2))
            elif trafficlight_dict["estadoE"][i] == GREEN:
                self.window.blit(self.greenE, (trafficlight_dict["SentEXMax"][i]-16, trafficlight_dict["SentEY"][i]+2))

            if trafficlight_dict["estadoO"][i] == RED:
                self.window.blit(self.redO, (trafficlight_dict["SentOXMin"][i]-4, trafficlight_dict["SentOY"][i]-16))
            elif trafficlight_dict["estadoO"][i] == GREEN:
                self.window.blit(self.greenO, (trafficlight_dict["SentOXMin"][i]-4, trafficlight_dict["SentOY"][i]-16))

            if trafficlight_dict["estadoN"][i] == RED:
                self.window.blit(self.redN, (trafficlight_dict["SentNX"][i]+2, trafficlight_dict["SentNYMin"][i]-4))
            elif trafficlight_dict["estadoN"][i] == GREEN:
                self.window.blit(self.greenN, (trafficlight_dict["SentNX"][i]+2, trafficlight_dict["SentNYMin"][i]-4))

            if trafficlight_dict["estadoS"][i] == RED:
                self.window.blit(self.redS, (trafficlight_dict["SentSX"][i]-16, trafficlight_dict["SentSYMax"][i]-16))
            elif trafficlight_dict["estadoS"][i] == GREEN:
                self.window.blit(self.greenS, (trafficlight_dict["SentSX"][i]-16, trafficlight_dict["SentSYMax"][i]-16))

        # Desenhar carros
        for i in range(len(car_dict["id"])):
            if car_dict["sentido"][i] == "E":
                self.window.blit(self.car_right, (car_dict["posx"][i]-18, car_dict["posy"][i]-8)) # Imagem do carro para este
            elif car_dict["sentido"][i] == "O":
                self.window.blit(self.car_left, (car_dict["posx"][i], car_dict["posy"][i]-8)) # Imagem do carro para oeste
            elif car_dict["sentido"][i] == "N":
                self.window.blit(self.car_up, (car_dict["posx"][i]-8, car_dict["posy"][i]-6)) # Imagem do carro para Norte
            elif car_dict["sentido"][i] == "S":
                self.window.blit(self.car_down, (car_dict["posx"][i]-8, car_dict["posy"][i]-22)) # Imagem do carro para Sul

        # Desenhar carros de emergência        
        for i in range(len(emergency_car_dict["id"])):
            if emergency_car_dict["sentido"][i] == "E":
                self.window.blit(self.emegency_car_right, (emergency_car_dict["posx"][i]-18, emergency_car_dict["posy"][i]-8)) # Imagem do carro para este
            elif emergency_car_dict["sentido"][i] == "O":
                self.window.blit(self.emegency_car_left, (emergency_car_dict["posx"][i], emergency_car_dict["posy"][i]-8)) # Imagem do carro para oeste
            elif emergency_car_dict["sentido"][i] == "N":
                self.window.blit(self.emegency_car_up, (emergency_car_dict["posx"][i]-8, emergency_car_dict["posy"][i]-6)) # Imagem do carro para Norte
            elif emergency_car_dict["sentido"][i] == "S":
                self.window.blit(self.emegency_car_down, (emergency_car_dict["posx"][i]-8, emergency_car_dict["posy"][i]-22)) # Imagem do carro para Sul    
        pygame.display.update()
    

    def createTrafficLight(environment, id, SentEY, SentEXMin, SentEXMax, SentOY, SentOXMin, SentOXMax, SentNX, SentNYMin, SentNYMax, SentSX, SentSYMin, SentSYMax, estadoN, estadoS, estadoO, estadoE):
        try:
            isRegister = trafficlight_dict["id"].index(id)
        except ValueError:
            isRegister = -1
        if isRegister == -1:
            trafficlight_dict["id"].append(id)
            trafficlight_dict["SentEY"].append(SentEY)
            trafficlight_dict["SentEXMin"].append(SentEXMin)
            trafficlight_dict["SentEXMax"].append(SentEXMax)
            trafficlight_dict["SentOY"].append(SentOY)
            trafficlight_dict["SentOXMin"].append(SentOXMin)
            trafficlight_dict["SentOXMax"].append(SentOXMax)
            trafficlight_dict["SentNX"].append(SentNX)
            trafficlight_dict["SentNYMin"].append(SentNYMin)
            trafficlight_dict["SentNYMax"].append(SentNYMax)
            trafficlight_dict["SentSX"].append(SentSX)
            trafficlight_dict["SentSYMin"].append(SentSYMin)
            trafficlight_dict["SentSYMax"].append(SentSYMax)
            trafficlight_dict["estadoN"].append(estadoN)
            trafficlight_dict["estadoS"].append(estadoS)
            trafficlight_dict["estadoO"].append(estadoO)
            trafficlight_dict["estadoE"].append(estadoE)
        else:
            print("Erro em createTrafficLight")
            
    def updateTrafficLight(id, estadoN, estadoS, estadoO, estadoE):
        id = str(id)
        try:
            isRegister = trafficlight_dict["id"].index(id)
        except ValueError:
            isRegister = -1
        if isRegister != -1:
            trafficlight_dict["estadoN"][isRegister] = estadoN
            trafficlight_dict["estadoS"][isRegister] = estadoS
            trafficlight_dict["estadoO"][isRegister] = estadoO
            trafficlight_dict["estadoE"][isRegister] = estadoE
        else:
            print("Erro em updateTrafficLight")


    def createCar(environment, id, posx, posy, sentido, status):
        try:
            isRegister = car_dict["id"].index(id)

        except ValueError:
            isRegister = -1
        if isRegister == -1:
            car_dict["id"].append(id)
            car_dict["posx"].append(posx)
            car_dict["posy"].append(posy)
            car_dict["sentido"].append(sentido)
            car_dict["status"].append(status)
        else:
            car_dict["posx"][isRegister] = posx
            car_dict["posy"][isRegister] = posy
            car_dict["sentido"][isRegister] = sentido
            car_dict["status"][isRegister] = status

    def createEmergencyCar(environment, id, posx, posy, sentido, status):
        try:
            isRegister = emergency_car_dict["id"].index(id)

        except ValueError:
            isRegister = -1
        if isRegister == -1:
            emergency_car_dict["id"].append(id)
            emergency_car_dict["posx"].append(posx)
            emergency_car_dict["posy"].append(posy)
            emergency_car_dict["sentido"].append(sentido)
            emergency_car_dict["status"].append(status)
        else:
            emergency_car_dict["posx"][isRegister] = posx
            emergency_car_dict["posy"][isRegister] = posy
            emergency_car_dict["sentido"][isRegister] = sentido
            emergency_car_dict["status"][isRegister] = status
    
    #def respawn(environment, x, y):
        

    def contar_carros(environment, jid_semaforo):
        contagemOE = 0
        contagemNS = 0
        jid_semaforo = str(jid_semaforo)
        id_semaforo = trafficlight_dict["id"].index(jid_semaforo)

        for i in range(len(car_dict["id"])):
            if ((trafficlight_dict["SentNYMin"][id_semaforo] <= car_dict["posy"][i] <= trafficlight_dict["SentNYMax"][id_semaforo] and car_dict["posx"][i] == trafficlight_dict["SentNX"][id_semaforo]) or (trafficlight_dict["SentSYMin"][id_semaforo] <= car_dict["posy"][i] <= trafficlight_dict["SentSYMax"][id_semaforo] and car_dict["posx"][i] == trafficlight_dict["SentSX"][id_semaforo])):
                contagemNS += 1
            elif ((trafficlight_dict["SentEXMin"][id_semaforo] <= car_dict["posx"][i] <= trafficlight_dict["SentEXMax"][id_semaforo] and car_dict["posy"][i] == trafficlight_dict["SentEY"][id_semaforo]) or (trafficlight_dict["SentOXMin"][id_semaforo] <= car_dict["posx"][i] <= trafficlight_dict["SentOXMax"][id_semaforo] and car_dict["posy"][i] == trafficlight_dict["SentOY"][id_semaforo])):
                contagemOE += 1 
        return contagemNS, contagemOE

    def contar_carros_emergencia(environment, jid_semaforo):
        contagemEmerOE = 0
        contagemEmerNS = 0
        jid_semaforo = str(jid_semaforo)
        id_semaforo = trafficlight_dict["id"].index(jid_semaforo)

        for i in range(len(emergency_car_dict["id"])):
            if ((trafficlight_dict["SentNYMin"][id_semaforo] <= emergency_car_dict["posy"][i] <= trafficlight_dict["SentNYMax"][id_semaforo] and emergency_car_dict["posx"][i] == trafficlight_dict["SentNX"][id_semaforo]) or (trafficlight_dict["SentSYMin"][id_semaforo] <= emergency_car_dict["posy"][i] <= trafficlight_dict["SentSYMax"][id_semaforo] and emergency_car_dict["posx"][i] == trafficlight_dict["SentSX"][id_semaforo])):
                contagemEmerNS += 1
            elif ((trafficlight_dict["SentEXMin"][id_semaforo] <= emergency_car_dict["posx"][i] <= trafficlight_dict["SentEXMax"][id_semaforo] and emergency_car_dict["posy"][i] == trafficlight_dict["SentEY"][id_semaforo]) or (trafficlight_dict["SentOXMin"][id_semaforo] <= emergency_car_dict["posx"][i] <= trafficlight_dict["SentOXMax"][id_semaforo] and emergency_car_dict["posy"][i] == trafficlight_dict["SentOY"][id_semaforo])):
                contagemEmerOE += 1
        return contagemEmerNS, contagemEmerOE

    def contar_carros_parados(environment, jid_semaforo):
        contagem_paradosOE = 0
        contagem_paradosNS = 0
        jid_semaforo = str(jid_semaforo)
        id_semaforo = trafficlight_dict["id"].index(jid_semaforo)

        for i in range(len(car_dict["id"])):
            if ((trafficlight_dict["SentNYMin"][id_semaforo] <= car_dict["posy"][i] <= trafficlight_dict["SentNYMax"][id_semaforo] and car_dict["posx"][i] == trafficlight_dict["SentNX"][id_semaforo]) or (trafficlight_dict["SentSYMin"][id_semaforo] <= car_dict["posy"][i] <= trafficlight_dict["SentSYMax"][id_semaforo] and car_dict["posx"][i] == trafficlight_dict["SentSX"][id_semaforo])) and car_dict["status"][i] == False:
                contagem_paradosNS += 1
            elif ((trafficlight_dict["SentEXMin"][id_semaforo] <= car_dict["posx"][i] <= trafficlight_dict["SentEXMax"][id_semaforo] and car_dict["posy"][i] == trafficlight_dict["SentEY"][id_semaforo]) or (trafficlight_dict["SentOXMin"][id_semaforo] <= car_dict["posx"][i] <= trafficlight_dict["SentOXMax"][id_semaforo] and car_dict["posy"][i] == trafficlight_dict["SentOY"][id_semaforo])) and car_dict["status"][i] == False:
                contagem_paradosOE += 1
        return contagem_paradosNS, contagem_paradosOE

    def obter_posicaocarro(self):
        return self.posicaocarro
    
    def obter_estado_semaforo(environment, x, y, status, sentido):
        carros_parados = 0

        if (x < 0 or x > 476) or (y < 0 or y > 476):
            return "Saiu da cidade"
        
        elif (((x==108 or x==336) and (y==124 or y==336)) and sentido=="E"):
            return "Direita"

        elif (((x==124 or x==352) and (y==108 or y==336)) and sentido=="O"):
            return "Direita"

        elif (((x==124 or x==352) and (y==124 or y==352)) and sentido=="N"):
            return "Direita"

        elif (((x==108 or x==336) and (y==108 or y==336)) and sentido=="S"):
            return "Direita"
        
        for i in range(len(trafficlight_dict["id"])):
            
            if trafficlight_dict["SentEY"][i] == y and trafficlight_dict["SentEXMin"][i] < x <= trafficlight_dict["SentEXMax"][i]:
                estado = trafficlight_dict["estadoE"][i]  # Estado para Leste
                
                if(estado == RED and status==True):
                    for carro in range(len(car_dict["id"])):
                        if trafficlight_dict["SentEY"][i] == car_dict["posy"][carro] and trafficlight_dict["SentEXMin"][i] < car_dict["posx"][carro] <= trafficlight_dict["SentEXMax"][i] and car_dict["status"][carro] == False:                                      
                            carros_parados += 1  # Incrementa o contador de carros parados no sentido leste
                    return trafficlight_dict["SentEXMax"][i] - (22 * carros_parados)
                elif(estado == RED and status==False):
                    return "Mantem parado que ainda está vermelho"
                else:
                    carros_parados = -1

            elif trafficlight_dict["SentOY"][i] == y and trafficlight_dict["SentOXMin"][i] <= x < trafficlight_dict["SentOXMax"][i]:
                estado = trafficlight_dict["estadoO"][i]  # Estado para Oeste
                
                if(estado == RED and status==True):
                    # Verifica se há carros dentro das coordenadas para o semáforo oeste
                    for carro in range(len(car_dict["id"])):
                        if trafficlight_dict["SentOY"][i] == car_dict["posy"][carro] and trafficlight_dict["SentOXMin"][i] <= car_dict["posx"][carro] < trafficlight_dict["SentOXMax"][i] and car_dict["status"][carro] == False:
                            carros_parados += 1  # Incrementa o contador de carros parados no sentido oeste
                    return trafficlight_dict["SentOXMin"][i] + (22 * carros_parados)
                elif(estado == RED and status==False):
                    return "Mantem parado que ainda está vermelho"
                else:
                    carros_parados = -1

            elif trafficlight_dict["SentNX"][i] == x and trafficlight_dict["SentNYMin"][i] <= y < trafficlight_dict["SentNYMax"][i]:
                estado = trafficlight_dict["estadoN"][i]  # Estado para Norte
                
                if(estado == RED and status==True):
                    # Verifica se há carros dentro das coordenadas para o semáforo norte
                    for carro in range(len(car_dict["id"])):
                        if trafficlight_dict["SentNX"][i] == car_dict["posx"][carro] and trafficlight_dict["SentNYMin"][i] <= car_dict["posy"][carro] < trafficlight_dict["SentNYMax"][i] and car_dict["status"][carro] == False:
                            carros_parados += 1  # Incrementa o contador de carros parados no sentido norte

                    return trafficlight_dict["SentNYMin"][i] + (22 * carros_parados)
                elif(estado == RED and status==False):
                    return "Mantem parado que ainda está vermelho"
                else:
                    carros_parados = -1

            elif trafficlight_dict["SentSX"][i] == x and trafficlight_dict["SentSYMin"][i] < y <= trafficlight_dict["SentSYMax"][i]:
                estado = trafficlight_dict["estadoS"][i]  # Estado para Sul
                if(estado == RED and status==True):
                    # Verifica se há carros dentro das coordenadas para o semáforo sul
                    for carro in range(len(car_dict["id"])):
                        if trafficlight_dict["SentSX"][i] == car_dict["posx"][carro] and trafficlight_dict["SentSYMin"][i] < car_dict["posy"][carro] <= trafficlight_dict["SentSYMax"][i] and car_dict["status"][carro] == False:
                            carros_parados += 1  # Incrementa o contador de carros parados no sentido sul
                    return trafficlight_dict["SentSYMax"][i] - (22 * carros_parados)
                elif(estado == RED and status==False):
                    return "Mantem parado que ainda está vermelho"
                else:
                    carros_parados = -1
        return -1
    
    def mostrar_informacoes_carros(car_dict):
        for i in range(len(car_dict["id"])):
            carro_id = car_dict["id"][i]
            pos_x = car_dict["posx"][i]
            pos_y = car_dict["posy"][i]
            sentido = car_dict["sentido"][i]
    