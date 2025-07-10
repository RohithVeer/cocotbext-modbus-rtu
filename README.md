cocotbext-MODBUS-RTU

A modular and reusable Verification IP (VIP) for verifying MODBUS RTU protocol implementations using the cocotb Python-based verification framework.

This VIP provides high-level drivers, monitors, scoreboards, error detection, and functional coverage to validate MODBUS RTU communication transactions at the byte and CRC level.
Key Features

    MODBUS RTU Frame Modeling — Constructs valid MODBUS frames including CRC-16.
    Driver & Monitor — Simulates master frame generation and captures responses.
    Scoreboard — Compares expected and received frames for validation.
    Error Checker — Performs CRC integrity checks.
    Coverage Collector — Tracks usage frequency of function codes.
    Modular VIP Architecture — Easily reusable across projects.

## Directory Structure

cocotbext-modbus/
├── cocotbext/
│ └── modbus/
│ ├── modbus_driver.py # MODBUS RTU Driver
│ ├── modbus_monitor.py # MODBUS RTU Monitor
│ ├── modbus_scoreboard.py # Scoreboard for frame comparison
│ ├── modbus_coverage.py # Coverage tracking
│ ├── modbus_rtu.py # CRC + Frame generator
│ ├── error_handling.py # CRC validator
│ └── modbus_bus.py # Signal abstraction (optional)
├── sim/
│ └── tlvhpd1250.v # Example DUT: Simple loopback interface
├── tb/
│ └── test_modbus_advanced.py # Top-level test integrating all VIP components
├── Makefile # cocotb Makefile
├── generate_test_report.py # Report generation script
└── test_reports/ # Auto-generated test reports (HTML & TXT)


## cocotbext-MODBUS-RTU

The included sample DUT (tlvhpd1250.v) represents a simple MODBUS RTU loopback interface. It echoes transmitted tx_data on the rx_data output when both tx_enable and rx_enable are active. This behavior is ideal for validating the correctness of transmitted and received frames, and it helps demonstrate:

    Correct frame structure

    Accurate CRC generation/validation

    Clean RX/TX signal interaction

## How to Run the Test
Prerequisites

Ensure the following tools are installed:

    Python 3.10+

    cocotb (≥1.7)

    Icarus Verilog (iverilog)

    pip dependencies from requirements.txt

## Steps to Simulate

# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the cocotb test
make MODULE=tb.test_modbus_advanced

## Generate Test Reports

python generate_test_report.py

After simulation, detailed results (status, timing, CRC errors, function code coverage) will be saved under:

    test_reports/test_report.txt

    test_reports/test_report.html

You can open the HTML file in any browser.
## Sample Report

Includes:

    Status of all test cases

    Frame match results

    CRC validation

    Function code coverage summary

## License

This project is licensed under the MIT License.

#Acknowledgements
Mentor: Vijayvithal Jahagirdar
