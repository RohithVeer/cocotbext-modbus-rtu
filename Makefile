# ============================================================================
# IS4310-based Modbus RTU VIP Makefile for Cocotb + Icarus Verilog + GTKWave
# ============================================================================

# Set Python module paths for Cocotb to locate testbench modules
export PYTHONPATH := $(PWD)/tb:$(PWD)

# ----------------------
# Cocotb Configuration
# ----------------------
MODULE         = tb.test_modbus_advanced  # Python testbench module
TOPLEVEL       = IS4310_1250              # Verilog top-level module (DUT)
TOPLEVEL_LANG  = verilog
VERILOG_SOURCES += $(PWD)/sim/IS4310_1250.v
SIM            = icarus                   # Icarus Verilog as simulator

# Include Cocotb simulation rules (this defines its own 'clean' target)
include $(shell cocotb-config --makefiles)/Makefile.sim

# ------------------------------
# Native Icarus Verilog Targets
# ------------------------------

iverilog_build:
	iverilog -g2012 -o sim.vvp sim/IS4310_1250.v

iverilog_run: iverilog_build
	vvp sim.vvp

view_waveform: iverilog_run
	gtkwave sim.vcd

# ---------------------
# Custom Clean Target
# ---------------------
.PHONY: clean_all iverilog_build iverilog_run view_waveform

clean_all:
	rm -rf sim_build sim.vvp sim.vcd test_reports results.xml

