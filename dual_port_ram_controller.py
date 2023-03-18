import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
async def test_dual_port_ram_controller(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())

    # Write to memory addresses 0 and 1
    dut.address_1 <= 0
    dut.address_2 <= 1
    dut.write_data_1 <= 0x123456789abcdef0
    dut.write_data_2 <= 0xaaaaaaaaaaaaaaaa
    dut.write_en <= 1

    # Wait for two clock cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Read from memory addresses 0 and 1
    dut.write_en <= 0
    await RisingEdge(dut.clk)
    assert dut.read_data_1.value == 0x123456789abcdef0
    assert dut.read_data_2.value == 0xaaaaaaaaaaaaaaaa

    # Write to memory addresses 2 and 3
    dut.address_1 <= 2
    dut.address_2 <= 3
    dut.write_data_1 <= 0xffffffffffffffff
    dut.write_data_2 <= 0x5555555555555555
    dut.write_en <= 1

    # Wait for two clock cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Read from memory addresses 2 and 3
    dut.write_en <= 0
    await RisingEdge(dut.clk)
    assert dut.read_data_1.value == 0xffffffffffffffff
    assert dut.read_data_2.value == 0x5555555555555555

    # Write to memory addresses 4 and 5
    dut.address_1 <= 4
    dut.address_2 <= 5
    dut.write_data_1 <= 0x123456789abcdef0
    dut.write_data_2 <= 0xaaaaaaaaaaaaaaaa
    dut.write_en <= 1

    # Wait for two clock cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Read from memory addresses 4 and 5
    dut.write_en <= 0
    await RisingEdge(dut.clk)
    assert dut.read_data_1.value == 0x123456789abcdef0
    assert dut.read_data_2.value == 0xaaaaaaaaaaaaaaaa