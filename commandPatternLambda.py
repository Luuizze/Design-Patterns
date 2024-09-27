# EQUIPE
# Antônio Horácio Rodrigues de Magalhães
# Carlos Henrique Racobaldo Luz Montes
# Luiz Guilherme Guerreiro Carvalho
# Maria Eduarda Lopes de Morais Brito
# Enzo Gebauer

from abc import ABC, abstractmethod

# Interface Command (não utilizada com lambdas, mas mantém o padrão de projeto se necessário)
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


# Classe RemoteControl com suporte a lambdas e botão undo
class RemoteControl:
    def __init__(self):
        self.on_commands = [None] * 7  # 7 slots para comandos ON
        self.off_commands = [None] * 7  # 7 slots para comandos OFF
        self.undo_command = None  # Armazena o último comando para o botão undo
    
    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
    
    def on_button_was_pushed(self, slot):
        if self.on_commands[slot]:
            self.on_commands[slot]()  # Chamamos a função diretamente
            self.undo_command = self.off_commands[slot]  # Para desfazer o último comando ON
    
    def off_button_was_pushed(self, slot):
        if self.off_commands[slot]:
            self.off_commands[slot]()  # Chamamos a função diretamente
            self.undo_command = self.on_commands[slot]  # Para desfazer o último comando OFF
    
    def undo_button_was_pushed(self):
        if self.undo_command:
            self.undo_command()  # Chamamos o último comando salvo


# Testar o controle remoto
if __name__ == "__main__":
    remote_control = RemoteControl()

    # Criar dispositivos
    living_room_light = Light()
    kitchen_light = Light()
    ceiling_fan = CeilingFan()
    garage_door = GarageDoor()
    stereo = Stereo()

    # Usar lambdas para definir os comandos
    remote_control.set_command(0, 
                               on_command=lambda: living_room_light.on(), 
                               off_command=lambda: living_room_light.off())
    
    remote_control.set_command(1, 
                               on_command=lambda: kitchen_light.on(), 
                               off_command=lambda: kitchen_light.off())
    
    remote_control.set_command(2, 
                               on_command=lambda: ceiling_fan.high(), 
                               off_command=lambda: ceiling_fan.off())
    
    remote_control.set_command(3, 
                               on_command=lambda: garage_door.open(), 
                               off_command=lambda: garage_door.close())
    
    remote_control.set_command(4, 
                               on_command=lambda: stereo.on(), 
                               off_command=lambda: stereo.off())

    # Testar o controle remoto
    print("--- Ligar luz da sala ---")
    remote_control.on_button_was_pushed(0)
    
    print("--- Desligar luz da sala ---")
    remote_control.off_button_was_pushed(0)

    print("--- Desfazer ---")
    remote_control.undo_button_was_pushed()

    print("--- Ligar ventilador ---")
    remote_control.on_button_was_pushed(2)

    print("--- Ligar estéreo ---")
    remote_control.on_button_was_pushed(4)

    print("--- Desfazer ---")
    remote_control.undo_button_was_pushed()

