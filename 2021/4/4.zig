const std = @import("std");

fn solve(allocator: *std.mem.Allocator, input: []const u8) ![2]usize {
    var arena = std.heap.ArenaAllocator.init(allocator);
    defer arena.deinit();
    const alloc = (&arena.allocator).alloc;

    const numsLen = std.mem.count(u8, input, ",") + 1;
    var nums = try alloc(u8, numsLen);

    const boardsLen = std.mem.count(u8, input, "\n") / 6;
    var boards = try alloc([5][5]u8, boardsLen);

    var it = std.mem.tokenize(input, ", \n");
    for (nums) |_, i| {
        nums[i] = try std.fmt.parseInt(u8, it.next().?, 10);
    }
    for (boards) |_, i| {
        var r: usize = 0;
        while (r < 5) : (r += 1) {
            var c: usize = 0;
            while (c < 5) : (c += 1) {
                boards[i][r][c] = try std.fmt.parseInt(u8, it.next().?, 10);
            }
        }
    }

    // For part1 if you transforms nums[i] = v into index[v] = i then a row or
    // column has bingo at turn max(index[v]), then a board is the minimum of
    // those.
    var index = try alloc(usize, nums.len);
    for (nums) |n, i| {
        index[n] = i;
    }

    var first: usize = nums.len;
    var last: usize = 0;
    var score1: usize = 0;
    var score2: usize = 0;
    for (boards) |board| {
        var bingo = nums.len;
        var a: usize = 0;
        while (a < 5) : (a += 1) {
            var max_row: usize = 0;
            var max_col: usize = 0;
            var b: usize = 0;
            while (b < 5) : (b += 1) {
                max_row = std.math.max(max_row, index[board[a][b]]);
                max_col = std.math.max(max_col, index[board[b][a]]);
            }
            bingo = std.math.min3(bingo, max_row, max_col);
        }

        var score: usize = 0;
        for (board) |row| {
            for (row) |n| {
                if (index[n] > bingo) {
                    score += n;
                }
            }
        }
        score *= nums[bingo];
        if (bingo < first) {
            first = bingo;
            score1 = score;
        }
        if (bingo >= last) {
            last = bingo;
            score2 = score;
        }
    }

    return [2]usize{ score1, score2 };
}

test "example" {
    const input =
        \\7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
        \\
        \\22 13 17 11  0
        \\8  2 23  4 24
        \\21  9 14 16  7
        \\6 10  3 18  5
        \\1 12 20 15 19
        \\
        \\3 15  0  2 22
        \\9 18 13 17  5
        \\19  8  7 25 23
        \\20 11 10 24  4
        \\14 21 16 12  6
        \\
        \\14 21 17 24  4
        \\10 16 15  9 19
        \\18  8 23 26 20
        \\22 11 13  6  5
        \\ 2  0 12  3  7
    ;

    const a = try solve(std.testing.allocator, input);
    try std.testing.expectEqual(a[0], 4512);
    try std.testing.expectEqual(a[1], 1924);
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = &arena.allocator;

    const input = @embedFile("input");
    const a = try solve(allocator, input);
    std.debug.print("1: {}\n2: {}\n", .{ a[0], a[1] });
}
