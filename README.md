
from pathlib import Path

# Create the README.md content
readme_content = """
# cocotbext-MODBUS-RTU

A reusable **Verification IP (VIP)** developed using [cocotb](https://github.com/cocotb/cocotb) for validating **MODBUS RTU protocol** on a Verilog-based DUT. This VIP simulates real-world Modbus communication between a master and a slave, with CRC checks, coverage sampling, scoreboard comparison, and error handling.

---

##  Why IS4310_1250?

The chosen DUT for simulation is `IS4310_1250`, a simplified Modbus-compatible RTL model designed to mimic core data reception and transmission behavior. This IC model was selected based on project needs for internal loopback testing and minimalistic design for verifying Modbus features.

---

##  Project Structure

cocotbext-modbus-rtu/
│
├── cocotbext/
│ └── modbus/
│ ├── init.py
│ ├── modbus_rtu.py # CRC, frame builder
│ ├── modbus_driver.py # Drives frames into DUT
│ ├── modbus_monitor.py # Captures responses
│ ├── modbus_scoreboard.py # Frame comparison
│ ├── modbus_coverage.py # Function code coverage
│ ├── modbus_bus.py # Port mapping
│ └── error_handling.py # CRC error checker
│
├── tb/
│ └── test_modbus_advanced.py # Full integration test
│
├── sim/
│ ├── IS4310_1250.v # RTL model of DUT
│ └── tb.v # Verilog testbench (for GTKWave)
│
├── test_reports/
│ ├── test_report.txt # Text summary (auto-generated)
│ └── test_report.html # HTML summary (auto-generated)
│
├── generate_test_report.py # Post-simulation report generator
├── Makefile # Cocotb + Icarus Makefile
├── README.md # ← This file
├── results.xml # Cocotb results (auto-generated)
└── .gitignore # Ignore build and sim artifacts

yaml
Always show details

Copy

---


##  VIP Features

-  **Reusable VIP modules**: Driver, Monitor, Scoreboard, Coverage, CRC Checker  
-  **End-to-End frame checking** with CRC16 integrity validation  
-  **Function code coverage tracking**  
-  **Loopback testing** on IS4310_1250 RTL DUT  
-  **Verilog + Python hybrid co-simulation using Cocotb**  
-  **HTML/Text Test Reports** post-simulation  
-  **Modular and scalable structure** for reuse in other Modbus projects  

---


##  How to Run Simulation

###  Requirements

- Python ≥ 3.7
- [Cocotb](https://github.com/cocotb/cocotb) ≥ 1.7
- Icarus Verilog (`iverilog`)
- GTKWave (`gtkwave`)

---


###  Installation

```bash
# Clone repo
git clone https://github.com/RohithVeer/cocotbext-modbus-rtu.git
cd cocotbext-modbus-rtu

# Install as editable package
pip install -e .
 Simulation Steps
🔹 Cocotb Test (Full Verification)
bash
Always show details

Copy
make
This command will:

Compile the DUT (IS4310_1250.v)

Run test from tb.test_modbus_advanced

Log frame TX/RX activity

Validate CRC

Generate coverage

Write results.xml

🔹 View Waveform in GTKWave (Optional)
bash
Always show details

Copy
make view_waveform
Tip: Add internal DUT signals to VCD using $dumpvars(0, tb.dut); inside tb.v.

🔹 Generate Reports
bash
Always show details

Copy
python generate_test_report.py
 test_reports/test_report.txt

 test_reports/test_report.html

 Test Behavior Summary
TX sends: Address = 2, Function Code = 0x04, Data = [1, 5]

CRC is appended automatically.

RX echoes the frame (loopback).

Monitor captures and Scoreboard compares it.

Coverage logs function code count.

CRC is validated.

Assertion checks ensure DUT behavior.

 Sample Log Snippet
vbnet
Always show details

Copy
TX byte: 2
TX byte: 4
TX byte: 1
TX byte: 5
TX byte: 129
TX byte: 206
Monitor captured frame: [2, 4, 1, 5, 129, 206]
CRC Validation PASSED.
Coverage: Function Code 0x04 count = 1
 Acknowledgements
Mentor: @jahagirdar – 

Inspired by: cocotbext

 Author
Rohith Mudigonda

 License
This project is licensed under the MIT License. See LICENSE file for details.
