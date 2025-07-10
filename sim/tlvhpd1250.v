module tlvhpd1250 (
    input        clk,
    input        reset,
    input        tx_enable,
    input  [7:0] tx_data,
    input        rx_enable,
    output reg [7:0] rx_data
);

always @(posedge clk or posedge reset) begin
    if (reset)
        rx_data <= 8'h00;
    else if (tx_enable && rx_enable)  // <-- synchronize properly
        rx_data <= tx_data;
    else
        rx_data <= 8'h00; // or 8'hZZ
end

initial begin
    $dumpfile("sim.vcd");
    $dumpvars(0, tlvhpd1250);
end

endmodule

