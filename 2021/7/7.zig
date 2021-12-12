const std = @import("std");

fn parseIntTokens(comptime T: type, buf: []T, it: anytype) ![]T {
    var i: usize = 0;
    while (it.next()) |n| {
        buf[i] = try std.fmt.parseInt(T, n, 10);
        i += 1;
    }
    return buf[0..i];
}

fn absDiff(x: anytype, y: anytype) @TypeOf(x, y) {
    return if (x < y) y - x else x - y;
}

fn solve(input: []const u8) ![2]usize {
    var buf = [_]usize{0} ** 1024;
    var it = std.mem.tokenize(input, " \n,");
    const nums = try parseIntTokens(usize, &buf, &it);

    var max = nums[0];
    var min = nums[0];
    for (nums) |n| {
        if (n > max)
            max = n;
        if (n < min)
            min = n;
    }
    var pos = min;
    var part1: usize = std.math.maxInt(usize);
    var part2: usize = std.math.maxInt(usize);
    while (pos <= max) : (pos += 1) {
        var v1: usize = 0;
        var v2: usize = 0;
        for (nums) |n| {
            const d = absDiff(n, pos);
            v1 += d;
            v2 += d * (d + 1) / 2;
        }

        part1 = std.math.min(part1, v1);
        part2 = std.math.min(part2, v2);
    }

    return [2]usize{ part1, part2 };
}

test "example" {
    const input = "16,1,2,0,4,2,7,1,2,14";

    const a = try solve(input);
    try std.testing.expectEqual(a[0], 37);
    try std.testing.expectEqual(a[1], 168);
}

pub fn main() !void {
    const input = @embedFile("input");
    const a = try solve(input);
    std.debug.print("Part1: {}\nPart2: {}\n", .{ a[0], a[1] });
}
