`timescale 1ns/1ps

module tb;

    reg clk = 0;
    reg reset = 0;
    reg tx_enable = 0;
    reg rx_enable = 0;
    reg [7:0] tx_data = 8'h00;
    wire [7:0] rx_data;
    wire [3:0] debug_counter;

    IS4310_1250 dut (
        .clk(clk),
        .reset(reset),
        .tx_enable(tx_enable),
        .tx_data(tx_data),
        .rx_enable(rx_enable),
        .rx_data(rx_data),
        .debug_counter(debug_counter)
    );

    always #5 clk = ~clk;

    initial begin
        reset = 1;
        #20;
        reset = 0;
        tx_enable = 1;
        rx_enable = 1;
        tx_data = 8'hA5;
        #40;
        tx_data = 8'h3C;
        #40;
        tx_enable = 0;
        rx_enable = 0;
        #100;
        $finish;
    end

    initial begin
        $dumpfile("sim.vcd");
        $dumpvars(0, tb);
    end

endmodule

