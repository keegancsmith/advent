const std = @import("std");

pub fn main() !void {
    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();
    var buf: [1024]u8 = undefined;
    var last: [3]u64 = .{1 << 63, 1 << 63, 1 << 63};
    var count1: u64 = 0;
    var count2: u64 = 0;
    while (try stdin.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        const trimmed = std.mem.trim(u8, line, "\n");
        const n = try std.fmt.parseInt(u64, trimmed, 10);
        if (n > last[2]) {
            count1 += 1;
        }
        if (n > last[0]) {
            count2 += 1;
        }
        last[0] = last[1];
        last[1] = last[2];
        last[2] = n;
    }
    try stdout.print("Part 1: {}\nPart 2: {}\n", .{count1, count2});
}
