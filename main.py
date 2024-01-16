import pygame
import sys
import asyncio
from environment import Environment
from traffic_light import TrafficLightAgent
from car import CarAgent
from emergency_car import EmergencyCar

async def main():
    pygame.init()
    ambiente_semaforo = Environment()
    
    trafficlight_agentC1 = TrafficLightAgent("traffic_lightc1@localhost", "secret", ambiente_semaforo, 104, 104, 124, 0, 100, 108, 130, 328, 124, 130, 328, 108, 0, 100)
    await trafficlight_agentC1.start()

    trafficlight_agentC2 = TrafficLightAgent("traffic_lightc2@localhost", "secret", ambiente_semaforo, 313, 104, 124, 130, 328, 108, 358, 456, 352, 130, 328, 336, 0, 100)
    await trafficlight_agentC2.start()

    trafficlight_agentC3 = TrafficLightAgent("traffic_lightc3@localhost", "secret", ambiente_semaforo, 104, 313, 352, 0, 100, 336, 130, 328, 124, 358, 456, 108, 130, 328)
    await trafficlight_agentC3.start()

    trafficlight_agentC4 = TrafficLightAgent("traffic_lightc4@localhost", "secret", ambiente_semaforo, 313, 313, 352, 130, 328, 336, 358, 456, 352, 358, 456, 336, 130, 328)
    await trafficlight_agentC4.start()

    carro_agent1 = CarAgent("car1@localhost", "secret", ambiente_semaforo, 352, 150, "N")
    await carro_agent1.start()

    carro_agent2 = EmergencyCar("car2@localhost", "secret", ambiente_semaforo, 352, 330, "N")
    await carro_agent2.start()

    carro_agent3 = CarAgent("car3@localhost", "secret", ambiente_semaforo, 308, 124, "E")
    await carro_agent3.start()

    carro_agent4 = CarAgent("car4@localhost", "secret", ambiente_semaforo, 278, 124, "E")
    await carro_agent4.start()

    carro_agent5 = CarAgent("car5@localhost", "secret", ambiente_semaforo, 248, 124, "E")
    await carro_agent5.start()
    
    carro_agent6 = CarAgent("car6@localhost", "secret", ambiente_semaforo, 0, 124, "E")
    await carro_agent6.start()

    carro_agent7 = CarAgent("car7@localhost", "secret", ambiente_semaforo, 352, 195, "N")
    await carro_agent7.start()

    carro_agent8 = CarAgent("car8@localhost", "secret", ambiente_semaforo, 108, 0, "S")
    await carro_agent8.start()

    carro_agent9 = CarAgent("car9@localhost", "secret", ambiente_semaforo, 124, 456, "N")
    await carro_agent9.start()

    carro_agent10 = CarAgent("car10@localhost", "secret", ambiente_semaforo, 50, 108, "O")
    await carro_agent10.start()

    running = True
    while running:
        ambiente_semaforo.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        await asyncio.sleep(0.016)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())