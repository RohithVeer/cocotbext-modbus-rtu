# cocotbext-MODBUS-RTU

A modular and reusable Verification IP (VIP) for verifying MODBUS RTU protocol implementations using the [cocotb](https://github.com/cocotb/cocotb) Python-based verification framework. This VIP includes drivers, monitors, scoreboards, and coverage components to simulate and verify MODBUS RTU communication at the byte and CRC level.

---

## Key Features

- **MODBUS RTU Transaction Modeling**: Frame construction, CRC calculation, and byte-wise transmission.
- **Driver & Monitor**: Simulates master behavior and listens to DUT responses.
- **Scoreboard**: Matches received data with expected results.
- **CRC Checker**: Validates CRC integrity of each frame.
- **Functional Coverage**: Tracks MODBUS function code utilization.
- **Modular Structure**: Reusable across various MODBUS-compliant DUTs.

---

## Directory Structure

#cocotbext-modbus/
├── cocotbext/
│ └── modbus/
│ ├── modbus_driver.py
│ ├── modbus_monitor.py
│ ├── modbus_scoreboard.py
│ ├── modbus_coverage.py
│ ├── modbus_rtu.py
│ ├── error_handling.py
│ └── modbus_bus.py
├── sim/
│ └── tlvhpd1250.v # Sample loopback DUT for testing
├── tb/
│ └── test_modbus_advanced.py # Integrated test with all components
├── Makefile
├── generate_test_report.py
└── test_reports/ # Auto-generated test reports


---

## Design Under Test (DUT)

We use `tlvhpd1250.v`, a simple Verilog-based MODBUS loopback design that reflects transmitted data back into the receiver channel. It validates the full verification pipeline by enabling:

- Clean Modbus frame transmission
- Receiver observation
- CRC validation and matching

This DUT ensures the VIP is agnostic and can be reused for other industrial-grade MODBUS implementations.

---

## How to Simulate

Ensure the following dependencies are installed:

- Python ≥ 3.10
- cocotb ≥ 1.7
- Icarus Verilog
---
Then run the following from the project root:
----
```bash
make MODULE=tb.test_modbus_advanced
---
You should see log outputs from:

    Frame transmission by the driver

    Frame capture by the monitor

    Scoreboard verification results

    CRC checks and coverage sampling
---
## Test Report Generation

After simulation, generate a detailed HTML and TXT report using:

python generate_test_report.py

Output files will be stored under test_reports/:

    test_report.txt: Plain-text summary

    test_report.html: Clickable HTML summary
---
Sample Test Output

800100.00ns INFO     cocotb  Scoreboard: Received frame recorded: [1, 3, 0, 2, 112, 25]
800100.00ns INFO     cocotb  CRC Validation PASSED.
800100.00ns INFO     cocotb  Coverage: Function Code 0x03 count = 1
800100.00ns INFO     cocotb  === Modbus Coverage Report ===
                          Function Code 0x03: 1 transaction(s)
800100.00ns INFO     cocotb  test_modbus_rtu_full_verification passed
---
License

This project is distributed under the MIT License.
Acknowledgements
[VijayvithaljahaGIRDAR](https://github.com/jahagirdar)
