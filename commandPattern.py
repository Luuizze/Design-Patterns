# EQUIPE
# Antônio Horácio Rodrigues de Magalhães
# Carlos Henrique Racobaldo Luz Montes
# Luiz Guilherme Guerreiro Carvalho
# Maria Eduarda Lopes de Morais Brito
# Enzo Gebauer

from abc import ABC, abstractmethod

# Interface Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receptor para a luz
class Light:
    def on(self):
        print("Light is ON")
        
    def off(self):
        print("Light is OFF")

# Receptor para o ventilador
class CeilingFan:
    def high(self):
        print("Ceiling fan is on HIGH")
        
    def off(self):
        print("Ceiling fan is OFF")

# Receptor para a garagem
class GarageDoor:
    def open(self):
        print("Garage door is OPEN")
        
    def close(self):
        print("Garage door is CLOSED")
        
# Receptor para o som
class Stereo:
    def on(self):
        print("Stereo is ON")
        
    def off(self):
        print("Stereo is OFF")


# Comando concreto para ligar a luz
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.on()

# Comando concreto para desligar a luz
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.off()

# Comando concreto para ligar o ventilador
class CeilingFanHighCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan
    
    def execute(self):
        self.fan.high()

# Comando concreto para abrir a garagem
class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door
    
    def execute(self):
        self.garage_door.open()

# Comando concreto para ligar o som
class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()


class RemoteControl:
    def __init__(self):
        self.on_commands = [None] * 7  # 7 slots para comandos ON
        self.off_commands = [None] * 7  # 7 slots para comandos OFF
    
    def set_command(self, slot, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
    
    def on_button_was_pushed(self, slot):
        if self.on_commands[slot]:
            self.on_commands[slot].execute()
    
    def off_button_was_pushed(self, slot):
        if self.off_commands[slot]:
            self.off_commands[slot].execute()


if __name__ == "__main__":
    remote_control = RemoteControl()

    # Criar dispositivos
    living_room_light = Light()
    kitchen_light = Light()
    ceiling_fan = CeilingFan()
    garage_door = GarageDoor()
    stereo = Stereo()

    # Criar comandos
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = LightOffCommand(kitchen_light)
    garage_door_open = GarageDoorOpenCommand(garage_door)
    stereo_on = StereoOnCommand(stereo)

    # Configurar o controle remoto
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_high, ceiling_fan_off)
    remote_control.set_command(3, garage_door_open, stereo_on)

    # Usar o controle remoto
    print("--- Ligar luz da sala ---")
    remote_control.on_button_was_pushed(0)
    
    print("--- Desligar luz da sala ---")
    remote_control.off_button_was_pushed(0)

    print("--- Ligar ventilador ---")
    remote_control.on_button_was_pushed(2)

    print("--- Ligar estéreo ---")
    remote_control.on_button_was_pushed(3)
