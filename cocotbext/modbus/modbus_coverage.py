import cocotb
from cocotbext.modbus.modbus_rtu import calculate_crc

class ModbusCoverage:
    def __init__(self):
        self.coverage = {}  # Dictionary to track function code occurrences

    def sample(self, frame: list):
        if len(frame) < 2:  # Ignore invalid frames
            return

        func_code = frame[1]  # Extract function code
        self.coverage[func_code] = self.coverage.get(func_code, 0) + 1  # Update function code count
        cocotb.log.info(f"Coverage: Function Code 0x{func_code:02X} count = {self.coverage[func_code]}")  # Log transaction count

    def report(self) -> str:
        report_str = "=== Modbus Coverage Report ===\n"  # Initialize report
        for code, count in self.coverage.items():  # Iterate over function codes
            report_str += f"Function Code 0x{code:02X}: {count} transaction(s)\n"  # Append stats
        cocotb.log.info(report_str)  # Log coverage summary
        return report_str

