from environment import Environment
from environment import trafficlight_dict, car_dict, emergency_car_dict
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


trafficLight_data = np.array([
    trafficlight_dict["SentEY"],
    trafficlight_dict["SentEXMin"],
    trafficlight_dict["SentEXMax"],
    trafficlight_dict["SentOY"],
    trafficlight_dict["SentOXMin"],
    trafficlight_dict["SentOXMax"],
    trafficlight_dict["SentNX"],
    trafficlight_dict["SentNYMin"],
    trafficlight_dict["SentNYMax"],
    trafficlight_dict["SentSX"],
    trafficlight_dict["SentSYMin"],
    trafficlight_dict["SentSYMax"],
    trafficlight_dict["estadoN"],
    trafficlight_dict["estadoS"],
    trafficlight_dict["estadoO"],
    trafficlight_dict["estadoE"],
], dtype=np.float32)

car_data = np.array([
    car_dict["posx"],
    car_dict["posy"],
    car_dict["sentido"],
    car_dict["status"]
], dtype=np.float32)

carEmergency_data = np.array([
    emergency_car_dict["posx"],
    emergency_car_dict["posy"],
    emergency_car_dict["sentido"],
    emergency_car_dict["status"]
], dtype=np.float32)

semaphore_tensor = torch.from_numpy(trafficLight_data.T)
car_tensor = torch.from_numpy(car_data.T)

target_tensor = torch.tensor(car_dict["status"], dtype=torch.float32)

class DisruptionManagementAgent:
    def __init__(self, environment):
        self.env = environment
        self.traffic_light_states = {}  # Dicionário para armazenar estados dos semáforos

    def handle_disruption(self, disruption_type):
        if disruption_type == "accident":
            print("Disruption detected: Accident")

        elif disruption_type == "road_closure":
            print("Disruption detected: Road closure")
            # Lógica para lidar com o fechamento de estrada (redirecionamento, etc.)

    def monitor_disruptions(self):
        for intersection_id, traffic_light in self.env.traffic_lights.items():
            current_state = traffic_light.get_state()  # Supondo método para obter o estado do semáforo

            # Verificar se há um semáforo quebrado ou não funcionando corretamente
            if current_state == "broken":
                self.handle_disruption("accident")  # Se um semáforo estiver quebrado, simular um acidente

disruption_agent = DisruptionManagementAgent(Environment)

# Monitorar continuamente as disrupções e tomar ação
while True:
    disruption_agent.monitor_disruptions()


