# cocotbext/modbus/modbus_bus.py
from cocotbext.modbus.modbus_rtu import calculate_crc

class ModbusBus:
    def __init__(self, entity, name):
        self.entity = entity
        self.rx = getattr(entity, f"{name}_rx")
        self.tx = getattr(entity, f"{name}_tx")  # Optional if bi-directional

