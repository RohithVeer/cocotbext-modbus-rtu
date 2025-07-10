import cocotb
from cocotbext.modbus.modbus_rtu import calculate_crc

class ModbusScoreboard:
    def __init__(self):
        self.expected = []  # Store expected Modbus transactions
        self.received = []  # Store received DUT responses

    def add_expected(self, frame: list):
        self.expected.append(frame)
        cocotb.log.info(f"Scoreboard: Expected frame recorded: {frame}")

    def add_received(self, frame: list):
        self.received.append(frame)
        cocotb.log.info(f"Scoreboard: Received frame recorded: {frame}")

    def compare(self):
        if len(self.expected) != len(self.received):
            cocotb.log.error("Mismatch in number of expected and received frames.")
            return False

        for exp, rec in zip(self.expected, self.received):
            if isinstance(exp, bytes):
                exp = list(exp)
            if exp != rec:
                cocotb.log.error(f"Mismatch: Expected {exp} vs Received {rec}")
                return False

        return True

