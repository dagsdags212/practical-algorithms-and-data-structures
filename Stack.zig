const std = @import("std");
const ArrayList = std.ArrayList;
const Allocator = std.mem.Allocator;

pub fn Stack(comptime T: type) type {
    return struct {
        stack: ArrayList(T),

        const Self = @This();

        pub fn init(allocator: Allocator) Self {
            return Self{ .stack = ArrayList(T).init(allocator) };
        }

        pub fn deinit(self: *Self) void {
            self.stack.deinit();
        }

        pub fn push(self: *Self, val: T) !void {
            try self.stack.append(val);
        }

        pub fn peek(self: *Self) ?T {
            if (self.stack.items.len == 0) {
                return null;
            }
            return self.stack.items[self.stack.items.len - 1];
        }

        pub fn pop(self: *Self) ?T {
            return self.stack.popOrNull();
        }

        pub fn size(self: *Self) usize {
            return self.stack.items.len;
        }

        pub fn isEmpty(self: *Self) bool {
            return self.size() == 0;
        }
    };
}

test {
    const expect = std.testing.expect;

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};

    const IntStack = Stack(i32);

    var stack = IntStack.init(gpa.allocator());
    defer stack.deinit();

    try stack.push(1);
    try stack.push(2);
    try stack.push(3);

    try expect(stack.isEmpty() == false);

    try expect(stack.peek().? == 3);
    try expect(stack.pop().? == 3);
    try expect(stack.peek().? == 2);
    try expect(stack.pop().? == 2);
    try expect(stack.peek().? == 1);
    try expect(stack.pop().? == 1);

    try expect(stack.isEmpty() == true);
}

pub fn main() !void {

    const allocator = std.heap.page_allocator;
    const IntStack = Stack(i32);
    var stack = IntStack.init(allocator);
    var i: i8 = 0;
    while (i <= 5) : (i += 1) {
        try stack.push(i);
    }
    std.debug.print("{}\n", stack);

}
