`timescale 1ns/1ps

module IS4310_1250 (
    input clk,
    input reset,
    input tx_enable,
    input [7:0] tx_data,
    input rx_enable,
    output reg [7:0] rx_data,
    output [3:0] debug_counter
);

    reg [3:0] internal_counter;

    assign debug_counter = internal_counter;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            rx_data <= 8'h00;
            internal_counter <= 4'b0000;
        end else if (tx_enable && rx_enable) begin
            rx_data <= tx_data;
            internal_counter <= internal_counter + 1;
        end else begin
            rx_data <= 8'h00;
        end
    end

endmodule

