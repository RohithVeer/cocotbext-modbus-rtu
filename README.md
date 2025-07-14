# cocotbext-modbus-rtu

A reusable **Verification IP (VIP)** for validating MODBUS RTU protocol behavior using the [cocotb](https://github.com/cocotb/cocotb) Python-based testbench framework. This VIP simulates real MODBUS transactions and checks frame integrity, CRC correctness, and functional coverage.

---

##  Why `IS4310_1250.v`?

The DUT (`IS4310_1250.v`) was selected to simulate basic Modbus functionality with synchronized `tx` and `rx` paths. This IC model echoes transmitted data when both `tx_enable` and `rx_enable` are active, ideal for validating VIP transaction and CRC checks.

---

##  Directory Structure

```
cocotbext-modbus-rtu/
│
├── cocotbext/
│   └── modbus/
│       ├── __init__.py
│       ├── modbus_rtu.py
│       ├── modbus_driver.py
│       ├── modbus_monitor.py
│       ├── modbus_scoreboard.py
│       ├── modbus_coverage.py
│       ├── error_handling.py
│
├── sim/
│   ├── IS4310_1250.v         # DUT (echo IC)
│   └── tb.v                  # Testbench for GTKWave
│
├── tb/
│   └── test_modbus_advanced.py
│
├── test_reports/
│   └── [auto-generated reports]
│
├── generate_test_report.py
├── Makefile
└── README.md
```

---

##  Features

- Full Modbus RTU transaction emulation.
- Real-time CRC16 validation.
- Transaction coverage logging per function code.
- Passive monitoring and driver scoreboarding.
- Compatibility with Icarus Verilog and GTKWave.

---

##  How to Use

###  1. Build & Simulate

```bash
make
```

###  2. Run the Icarus/Native Verilog testbench (non-cocotb)

```bash
make view_waveform
```

###  3. Generate Test Reports

```bash
python3 generate_test_report.py
```

###  4. Clean the Workspace

```bash
make clean
```

---

##  Testcase Flow

The testcase `test_modbus_rtu_full_verification` does the following:

1. Initializes driver, monitor, scoreboard, and coverage.
2. Sends a Modbus frame from the driver.
3. Monitor passively captures the echoed frame.
4. CRC is verified and logged.
5. Scoreboard matches expected vs received.
6. Functional coverage and logs are generated.

---

##  Acknowledgements

Special thanks to [@jahagirdar](https://github.com/jahagirdar) for valuable mentorship and guidance throughout the project.

---

##  Notes

- Developed using [cocotb v1.8.1](https://github.com/cocotb/cocotb).
- Tested on Ubuntu 22.04 LTS with Python 3.10 and GTKWave.
- IS4310_1250.v is a placeholder IC to test Modbus frame behavior.

---

##  Installation (as Python Package)

To install and use as a package:

```bash
pip install -e .
```
