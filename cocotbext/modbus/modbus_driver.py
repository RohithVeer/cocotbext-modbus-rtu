import cocotb
from cocotb.triggers import Timer
from cocotbext.modbus.modbus_rtu import calculate_crc


class ModbusRTUDriver:
    def __init__(self, dut):
        self.dut = dut  # Store reference to DUT interface

    async def send_frame(self, address: int, function_code: int, data_bytes: list, baud_delay: int = 10):
        frame = [address, function_code] + data_bytes  # Build Modbus frame (without CRC)
        crc = calculate_crc(bytes(frame))  # Compute CRC checksum
        full_frame = frame + list(crc)  # Append CRC bytes
        
        self.dut.tx_enable.value = 1  # Enable TX for data transmission
        for byte in full_frame:  # Transmit frame byte-by-byte
            self.dut.tx_data.value = byte  # Assign byte value to DUT TX port
            await Timer(baud_delay, units="us")  # Simulate baud rate delay
        self.dut.tx_enable.value = 0  # Disable TX after sending

        cocotb.log.info(f"Driver sent frame: {full_frame}")  # Log transaction details

