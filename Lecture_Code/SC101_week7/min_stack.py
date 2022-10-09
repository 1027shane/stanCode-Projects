class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Method 1:
        self.ds = []
        # Method 2:
        self.minStack = []

    def push(self, val: int) -> None:
        # Method 1:
        self.ds.append(val)
        # Method 2:
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        if len(self.ds) != 0:
            # Method 1:
            self.ds.pop()
            # Method 2:
            self.minStack.pop()

    def top(self) -> int:
        if len(self.ds) != 0:
            return self.ds[-1]

    def get_min(self) -> int:
        if len(self.ds) != 0:
            # Method 1:
            # my_min = self.ds[0]
            # for ele in self.ds:
            #     if ele < my_min:
            #         my_min = ele
            # return my_min

            # Method 2:
            return self.minStack[-1]


if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')      # [] --> return None
    print(my_stack.get_min(), end=', ')
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')  # -1
    print(my_stack.top(), end=', ')      # 3
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')  # -2
    print(my_stack.top())                # -2
