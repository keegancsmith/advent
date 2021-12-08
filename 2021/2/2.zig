const std = @import("std");
const testing = std.testing;

const Direction = enum {
    forward,
    up,
    down,
};

const Command = struct {
    direction: Direction,
    value: i64,
};

fn parseCommand(line: []const u8) !Command {
    var it = std.mem.tokenize(line, " \n");

    var direction: Direction = undefined;
    if (it.next()) |str| {
        if (std.mem.eql(u8, str, "forward")) {
            direction = Direction.forward;
        } else if (std.mem.eql(u8, str, "up")) {
            direction = Direction.up;
        } else if (std.mem.eql(u8, str, "down")) {
            direction = Direction.down;
        } else {
            return error.InvalidCharacter;
        }
    } else {
        return error.InvalidCharacter;
    }

    const value = if (it.next()) |str| try std.fmt.parseInt(i64, str, 10) else return error.InvalidCharacter;

    return Command{
        .direction = direction,
        .value = value,
    };
}

test "parseCommand" {
    try testing.expectEqual(try parseCommand("forward 5\n"), .{ .direction = Direction.forward, .value = 5 });
    try testing.expectEqual(try parseCommand("up 3\n"), .{ .direction = Direction.up, .value = 3 });
    try testing.expectEqual(try parseCommand("down 8\n"), .{ .direction = Direction.down, .value = 8 });

    try testing.expectError(error.InvalidCharacter, parseCommand(""));
    try testing.expectError(error.InvalidCharacter, parseCommand("hello\n"));
    try testing.expectError(error.InvalidCharacter, parseCommand("forward"));
    try testing.expectError(error.InvalidCharacter, parseCommand("forward five"));
}

fn part1(commands: []const Command) i64 {
    var x: i64 = 0;
    var y: i64 = 0;
    for (commands) |command| {
        const v = command.value;
        switch (command.direction) {
            Direction.forward => x += v,
            Direction.up => y -= v,
            Direction.down => y += v,
        }
    }
    return x * y;
}

fn part2(commands: []const Command) i64 {
    var aim: i64 = 0;
    var x: i64 = 0;
    var y: i64 = 0;
    for (commands) |command| {
        const v = command.value;
        switch (command.direction) {
            Direction.forward => {
                x += aim * v;
                y += v;
            },
            Direction.up => aim -= v,
            Direction.down => aim += v,
        }
    }
    return x * y;
}

test "example" {
    const example = [_]Command{
        .{ .direction = Direction.forward, .value = 5 },
        .{ .direction = Direction.down, .value = 5 },
        .{ .direction = Direction.forward, .value = 8 },
        .{ .direction = Direction.up, .value = 3 },
        .{ .direction = Direction.down, .value = 8 },
        .{ .direction = Direction.forward, .value = 2 },
    };

    try testing.expectEqual(part1(example[0..]), 150);
    try testing.expectEqual(part2(example[0..]), 900);
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();

    const allocator = &arena.allocator;

    const stdout = std.io.getStdOut().writer();
    const file = try std.fs.cwd().openFile("input", .{ .read = true });
    defer file.close();
    const input = file.reader();

    var commands = std.ArrayList(Command).init(allocator);
    defer commands.deinit();

    var buf: [1024]u8 = undefined;
    while (try input.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        try commands.append(try parseCommand(line));
    }
    try stdout.print("Part 1: {}\nPart 2: {}\n", .{ part1(commands.items), part2(commands.items) });
}
