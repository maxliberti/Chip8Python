class CPU:
    def __init__(self):
        self.memory = bytearray(4096) # 4kb of RAM
        self.registers = [0x00] * 16 # 16 register slots

cpu = CPU()

