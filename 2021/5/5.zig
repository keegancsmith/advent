const std = @import("std");

const Line = struct {
    ax: i32,
    ay: i32,
    bx: i32,
    by: i32,
};

fn cmp(x: anytype, y: anytype) i2 {
    if (x == y) {
        return 0;
    } else if (x < y) {
        return 1;
    } else {
        return -1;
    }
}

fn solve(allocator: *std.mem.Allocator, input: []const u8) ![2]usize {
    var lines = std.ArrayList(Line).init(allocator);
    defer lines.deinit();

    var it = std.mem.tokenize(input, ", ->\n");
    while (it.next()) |s| {
        try lines.append(Line{
            .ax = try std.fmt.parseInt(i32, s, 10),
            .ay = try std.fmt.parseInt(i32, it.next().?, 10),
            .bx = try std.fmt.parseInt(i32, it.next().?, 10),
            .by = try std.fmt.parseInt(i32, it.next().?, 10),
        });
    }

    var count = [_][1000]usize{[_]usize{0} ** 1000} ** 1000;
    for (lines.items) |l| {
        const dx: i32 = cmp(l.ax, l.bx);
        const dy: i32 = cmp(l.ay, l.by);
        if (dx != 0 and dy != 0)
            continue;
        var x = l.ax;
        var y = l.ay;
        while (x != l.bx or y != l.by) {
            count[@intCast(usize, x)][@intCast(usize, y)] += 1;
            x += dx;
            y += dy;
        }
        count[@intCast(usize, l.bx)][@intCast(usize, l.by)] += 1;
    }

    var part1: usize = 0;
    for (count) |row| {
        for (row) |c| {
            if (c >= 2) {
                part1 += 1;
            }
        }
    }

    // We duplicate part 1, but update count with only diagonals.
    for (lines.items) |l| {
        const dx: i32 = cmp(l.ax, l.bx);
        const dy: i32 = cmp(l.ay, l.by);
        if (dx == 0 or dy == 0)
            continue;
        var x = l.ax;
        var y = l.ay;
        while (x != l.bx or y != l.by) {
            count[@intCast(usize, x)][@intCast(usize, y)] += 1;
            x += dx;
            y += dy;
        }
        count[@intCast(usize, l.bx)][@intCast(usize, l.by)] += 1;
    }

    var part2: usize = 0;
    for (count) |row| {
        for (row) |c| {
            if (c >= 2) {
                part2 += 1;
            }
        }
    }

    return [2]usize{ part1, part2 };
}

test "example" {
    const input =
        \\0,9 -> 5,9
        \\8,0 -> 0,8
        \\9,4 -> 3,4
        \\2,2 -> 2,1
        \\7,0 -> 7,4
        \\6,4 -> 2,0
        \\0,9 -> 2,9
        \\3,4 -> 1,4
        \\0,0 -> 8,8
        \\5,5 -> 8,2
    ;

    const a = try solve(std.testing.allocator, input);
    try std.testing.expectEqual(a[0], 5);
    try std.testing.expectEqual(a[1], 12);
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();

    const input = @embedFile("input");
    const a = try solve(&arena.allocator, input);
    std.debug.print("{}\n{}\n", .{ a[0], a[1] });
}
