import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from cocotbext.modbus.modbus_driver import ModbusRTUDriver
from cocotbext.modbus.modbus_monitor import ModbusRTUMonitor
from cocotbext.modbus.modbus_scoreboard import ModbusScoreboard
from cocotbext.modbus.modbus_coverage import ModbusCoverage
from cocotbext.modbus.error_handling import ModbusErrorChecker
from cocotbext.modbus.modbus_rtu import build_modbus_frame

@cocotb.test()
async def test_modbus_rtu_full_verification(dut):
    """
    Full verification test integrating driver, monitor, scoreboard, and coverage.
    Reconfigurable via config dictionary.
    """

    # === Reconfigurable VIP Settings ===
    config = {
        'address': 2,              # Modbus address (user can override)
        'function_code': 0x04,     # Function code (user can override)
        'data_bytes': [0x01, 0x05],# Data payload (user can override)
        'baud_delay': 50,          # Baud delay (user can override)
        'frame_length': 6          # Frame length (user can override)
    }

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset DUT
    dut.reset.value = 1
    dut.tx_enable.value = 0
    dut.rx_enable.value = 0
    dut.tx_data.value = 0
    await Timer(100, units="ns")
    dut.reset.value = 0
    await RisingEdge(dut.clk)

    # Initialize VIPs with config for reconfigurability
    driver = ModbusRTUDriver(dut, config)
    monitor = ModbusRTUMonitor(dut, config)
    scoreboard = ModbusScoreboard()
    coverage = ModbusCoverage()
    error_checker = ModbusErrorChecker()

    # Modbus transaction (all parameters from config)
    address = config['address']
    function_code = config['function_code']
    data_bytes = config['data_bytes']
    expected_frame = build_modbus_frame(address, function_code, data_bytes)
    scoreboard.add_expected(list(expected_frame))

    cocotb.log.info(f"Transmitting frame: {list(expected_frame)}")

    # Start monitor first
    monitor_task = cocotb.start_soon(
        monitor.capture_frame(expected_length=len(expected_frame), baud_delay=config['baud_delay'])
    )

    # Delay to ensure monitor is listening
    await Timer(100, units="us")

    # Drive frame from DUT interface (simulate TX)
    dut.tx_enable.value = 1
    for byte in expected_frame:
        cocotb.log.info(f"TX byte: {byte}")
        dut.tx_data.value = byte
        await Timer(config['baud_delay'], units="us")
    dut.tx_enable.value = 0

    # Allow time for monitor
    await Timer(100, units="us")

    received_frame = await monitor_task
    scoreboard.add_received(received_frame)
    error_checker.check_errors(received_frame)
    coverage.sample(received_frame)

    assert scoreboard.compare(), "ERROR: Expected and received transactions do not match!"
    coverage.report()

