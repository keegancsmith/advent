const std = @import("std");

const Location = struct {
    val: u8,
    pos: usize,
};

const Basin = struct {
    input: []const u8,
    _cols: isize = -1,

    fn init(self: *Basin) void {
        self.input = std.mem.trim(u8, self.input, " \n");
        self._cols = @intCast(isize, std.mem.indexOfScalar(u8, self.input, '\n') orelse self.input.len);
    }

    pub fn neigh(self: *Basin, buf: *[4]Location, pos: usize) []Location {
        if (self._cols == -1)
            self.init();

        const i = @intCast(isize, pos);
        var len: usize = 0;
        const deltas = [_]isize{ -1, 1, -self._cols - 1, self._cols + 1 };
        for (deltas) |d| {
            const j: isize = i + d;
            if (j < 0 or j >= self.input.len)
                continue;
            const neigh_pos = @intCast(usize, j);
            if (self.input[neigh_pos] != '\n') {
                buf[len] = Location{
                    .val = self.input[neigh_pos],
                    .pos = neigh_pos,
                };
                len += 1;
            }
        }
        return buf[0..len];
    }
};

fn solve(input: []const u8) ![2]usize {
    var basin = Basin{ .input = input };
    basin.init();

    var neigh_buf: [4]Location = undefined;

    var part1: usize = 0;
    for (basin.input) |v, i| {
        if (v == '\n') {
            continue;
        }
        const is_low = for (basin.neigh(&neigh_buf, i)) |neigh| {
            if (neigh.val <= v)
                break false;
        } else true;

        if (is_low) {
            part1 += v + 1 - '0';
        }
    }

    return [2]usize{ part1, 0 };
}

test "example" {
    const input =
        \\2199943210
        \\3987894921
        \\9856789892
        \\8767896789
        \\9899965678
    ;

    const a = try solve(input);
    try std.testing.expectEqual(a[0], 15);
    //try std.testing.expectEqual(a[1], 168);
}

pub fn main() !void {
    const input = @embedFile("input");
    const a = try solve(input);
    std.debug.print("Part1: {}\nPart2: {}\n", .{ a[0], a[1] });
}
