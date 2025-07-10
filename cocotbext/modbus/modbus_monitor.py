import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

class ModbusRTUMonitor:
    def __init__(self, dut):
        self.dut = dut
        self.received_frames = []

    async def capture_frame(self, expected_length: int, baud_delay: int = 100):
        """Capture Modbus frame ignoring 'x'/'z' and waiting for non-zero start."""
        self.dut.rx_enable.value = 1
        frame = []

        # Wait for non-zero valid byte to start
        while True:
            val = self.dut.rx_data.value
            if isinstance(val, BinaryValue) and ('x' in str(val) or 'z' in str(val)):
                await Timer(baud_delay, units="us")
                continue
            try:
                byte_val = int(val)
                if byte_val != 0:
                    frame.append(byte_val)
                    break
            except:
                pass
            await Timer(baud_delay, units="us")

        # Continue capturing the rest
        while len(frame) < expected_length:
            await Timer(baud_delay, units="us")
            val = self.dut.rx_data.value
            try:
                byte_val = int(val)
                frame.append(byte_val)
            except:
                continue

        self.dut.rx_enable.value = 0
        self.received_frames.append(frame)
        cocotb.log.info(f"Monitor captured frame: {frame}")
        return frame

