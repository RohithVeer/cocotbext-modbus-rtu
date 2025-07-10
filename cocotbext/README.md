# cocotbext-MODBUS-RTU

A reusable **Verification IP (VIP)** for testing **MODBUS RTU protocol** using the [Cocotb](https://github.com/cocotb/cocotb) framework. This VIP provides a full suite including driver, monitor, scoreboard, CRC checker, and functional coverage to validate MODBUS RTU communication.

---

## ✅ What This VIP Does

- Sends and receives MODBUS RTU frames
- Checks CRC correctness
- Compares actual vs expected results
- Tracks which MODBUS functions are used
- Supports integration with any MODBUS-compliant DUT

---

## 📁 Project Structure

cocotbext-modbus/
├── cocotbext/modbus/ # VIP modules
│ ├── modbus_driver.py # Sends frames
│ ├── modbus_monitor.py # Captures DUT output
│ ├── modbus_scoreboard.py # Verifies results
│ ├── modbus_coverage.py # Logs function code usage
│ ├── modbus_rtu.py # Frame + CRC generator
│ ├── error_handling.py # Checks CRC integrity
│ └── modbus_bus.py # Signal abstraction
├── sim/tlvhpd1250.v # Example DUT (loopback)
├── tb/test_modbus_advanced.py# Main test case
├── generate_test_report.py # Report generator
├── test_reports/ # Stores HTML + text reports
└── Makefile # Build + simulate


---

## 🔧 How to Run Simulation

1. Install dependencies:
   - Python ≥ 3.10
   - cocotb ≥ 1.7
   - Icarus Verilog

2. Run the test:
   ```bash
   make MODULE=tb.test_modbus_advanced

📝 Generate Report

After simulation:

python generate_test_report.py

    test_reports/test_report.txt – Plain summary

    test_reports/test_report.html – Clickable HTML report

🧪 Design Under Test (DUT)

We use tlvhpd1250.v, a simple Verilog module that echoes transmitted frames back. This verifies:

    Frame integrity

    CRC correctness

    Timing & synchronization

You can replace this with your own MODBUS IP!
🧠 Why Use This?

    Modular: Plug-and-play with any MODBUS RTL design

    Accurate: Includes proper CRC validation

    Complete: Scoreboard + Coverage built in

    Open: MIT License for unrestricted use

👨‍💻 Author


Developed under the guidance of Vijayvithal Jahagirdar
📜 License

MIT License – Free to use, modify, and distribute.
