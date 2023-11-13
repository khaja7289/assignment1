module xor_test(
	input wire a,
	input wire b,
	output wire y
);
dut dut(
	.a(a),
	.b(b),
	.y(y)
);

initial begin
  $dumpfile("xor.vcd");
	$dumpvars;
end
endmodule
