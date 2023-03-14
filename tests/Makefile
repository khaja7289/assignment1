SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/xor.v
VERILOG_SOURCES += $(PWD)/wrappers/xor_test.v
TOPLEVEL = xor_test
MODULE = xor
include $(shell cocotb-config --makefiles)/Makefile.sim
