export PYTHONPATH := $(PWD)/tb:$(PWD)

MODULE = tb.test_modbus_advanced
TOPLEVEL = tlvhpd1250
TOPLEVEL_LANG = verilog
VERILOG_SOURCES += $(PWD)/sim/tlvhpd1250.v
SIM = icarus

include $(shell cocotb-config --makefiles)/Makefile.sim

