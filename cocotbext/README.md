 #cocotbext-MODBUS-RTU 

A modular and reusable Verification IP (VIP) for verifying MODBUS RTU protocol implementations using the [cocotb](https://github.com/cocotb/cocotb) Python-based verification framework. This VIP includes drivers, monitors, scoreboards, and coverage components to simulate and verify MODBUS RTU communication at the byte and CRC level.

---

#Key Features

- **MODBUS RTU Transaction Modeling**: Supports frame construction, CRC calculation, and transmission.
- **Driver & Monitor**: Simulates master behavior and observes responses from the DUT.
- **Scoreboard**: Validates received frames against expected results.
- **Error Checker**: Performs CRC integrity checks and logs mismatches.
- **Functional Coverage**: Tracks usage of MODBUS function codes.
- **Modular Structure**: Easy to plug-and-play with different MODBUS DUTs.

---

#Directory Structure

```bash
cocotbext-modbus/
├── cocotbext/
│   └── modbus/
│       ├── modbus_driver.py       # MODBUS RTU Driver
│       ├── modbus_monitor.py      # MODBUS RTU Monitor
│       ├── modbus_scoreboard.py   # Scoreboard for frame comparison
│       ├── modbus_coverage.py     # Coverage tracking
│       ├── modbus_rtu.py          # CRC + Frame generator
│       ├── error_handling.py      # CRC validator
│       └── modbus_bus.py          # Signal abstraction (optional)
├── sim/
│   └── tlvhpd1250.v               # Example DUT: Simple loopback interface
├── tb/
│   └── test_modbus_advanced.py    # Top-level test integrating all VIP components
├── Makefile                       # cocotb Makefile
├── results.xml                    # Test results file (generated)
└── test_reports/                  # Generated test reports (text & HTML)

# Design Under Test (DUT)

The VIP has been validated with a sample Verilog module tlvhpd1250.v, which emulates a simple MODBUS loopback mechanism. This DUT mirrors transmitted frames onto the receiver path, providing a controlled environment to evaluate the VIP's correctness in framing, CRC checking, and coverage.

Although this DUT is illustrative, the VIP is agnostic to DUT internals and can be adapted to industrial MODBUS IPs.
 How to Run

Ensure cocotb, Icarus Verilog, and Python 3.10+ are installed in your environment.

make MODULE=tb.test_modbus_advanced

#To generate the test report after simulation:

python generate_test_report.py

HTML and TXT reports will be created under the test_reports/ directory.

#Sample Test Report

Test and coverage results are saved automatically after simulation.

Report Preview:
 Click to View HTML Report
#License

This project is licensed under the MIT License.
# Acknowledgements

Vijayvithal Jahagirdar: for mentoring and providing guidance throughout the development process

   
