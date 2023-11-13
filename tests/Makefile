SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/wrappers/xor_test.v
TOPLEVEL = xor_test
MODULE = dut_test
include $(shell cocotb-config --makefiles)/Makefile.sim
