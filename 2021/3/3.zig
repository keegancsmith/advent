const std = @import("std");

fn parse(buf: [][]const u8, input: []const u8) [][]const u8 {
    var i: usize = 0;
    var it = std.mem.tokenize(input, "\n ");
    while (it.next()) |num| {
        buf[i] = num[0..];
        i += 1;
    }
    return buf[0..i];
}

fn part1(nums: [][]const u8) u64 {
    var gamma: u64 = 0;
    var epsilon: u64 = 0;
    for (nums[0]) |_, i| {
        var ones: usize = 0;
        for (nums) |num| {
            if (num[i] == '1') {
                ones += 1;
            }
        }
        gamma = gamma << 1;
        epsilon = epsilon << 1;
        if (ones * 2 >= nums.len) {
            gamma += 1;
        } else {
            epsilon += 1;
        }
    }
    return gamma * epsilon;
}

fn rating(numsIn: [][]const u8, bit: u8) []const u8 {
    var nums = numsIn[0..];
    for (nums[0]) |_, i| {
        var count: usize = 0;
        for (nums) |num, j| {
            if (num[i] == bit) {
                if (j != count) {
                    nums[j] = nums[count];
                    nums[count] = num;
                }
                count += 1;
            }
        }
        if ((bit == '1' and count * 2 >= nums.len) or (bit == '0' and count * 2 <= nums.len)) {
            nums = nums[0..count];
        } else {
            nums = nums[count..];
        }
        if (nums.len == 1) {
            break;
        }
    }
    return nums[0];
}

fn parseBinary(s: []const u8) u64 {
    var n: u64 = 0;
    for (s) |b| {
        n = n << 1;
        if (b == '1') {
            n += 1;
        }
    }
    return n;
}

fn part2(nums: [][]const u8) u64 {
    var o = rating(nums, '1');
    var co2 = rating(nums, '0');
    return parseBinary(o) * parseBinary(co2);
}

test "example" {
    const input =
        \\00100
        \\11110
        \\10110
        \\10111
        \\10101
        \\01111
        \\00111
        \\11100
        \\10000
        \\11001
        \\00010
        \\01010
    ;
    var buf: [1000][]const u8 = undefined;
    const nums = parse(buf[0..], input);

    try std.testing.expectEqual(part1(nums), 198);
    try std.testing.expectEqual(part2(nums), 230);
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();

    const allocator = &arena.allocator;

    const input = try std.fs.cwd().readFileAlloc(allocator, "input", 1024 * 1024);
    var buf: [1000][]const u8 = undefined;
    const nums = parse(buf[0..], input);

    var ans = part1(nums);
    try std.io.getStdOut().writer().print("Part 1: {}\n", .{ans});

    ans = part2(nums);
    try std.io.getStdOut().writer().print("Part 2: {}\n", .{ans});
}
