import pygame

class CHIP8:
    def __init__(self):
        self.memory = [0x000] * 4096
        self.registers = [0x00] * 16
        self.registers[0xF] = False # VF
        self.stack = [0] * 16
        self.pc = 0
        self.delayTimer = 0
        self.soundTimer = 0
        self.keypad = [0] * 16
        self.video = [ [0]*64 for i in range(32) ]
        self.opcode = 0






def main():
    screen = pygame.display.set_mode((64, 32))
    pygame.display.set_caption("CHIP 8")
    screen.fill((255, 255, 255))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    chip8 = CHIP8()
    print(chip8.registers)

if __name__ == "__main__":
    main()

