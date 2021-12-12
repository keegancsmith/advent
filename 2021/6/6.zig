const std = @import("std");

fn solve(input: []const u8, days: usize) !usize {
    var nums = [_]usize{0} ** 9;

    var it = std.mem.tokenize(input, " ,\n");
    while (it.next()) |n| {
        nums[try std.fmt.parseInt(usize, n, 10)] += 1;
    }

    var day: usize = 0;
    while (day < days) : (day += 1) {
        nums[(day + 7) % nums.len] += nums[day % nums.len];
    }

    var sum: usize = 0;
    for (nums) |n| {
        sum += n;
    }
    return sum;
}

test "example" {
    const input = "3,4,3,1,2";

    try std.testing.expectEqual(try solve(input, 18), 26);
    try std.testing.expectEqual(try solve(input, 80), 5934);
    try std.testing.expectEqual(try solve(input, 256), 26984457539);
}

pub fn main() !void {
    const input = @embedFile("input");

    std.debug.print("part1: {}\n", .{try solve(input, 80)});
    std.debug.print("part2: {}\n", .{try solve(input, 256)});
}
