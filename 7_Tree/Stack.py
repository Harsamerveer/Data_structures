from collections import deque


class Stack:

    def __init__(self):
        self.data = deque()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

def revere_string_function(txt):

    stack = Stack()

    for i in txt:
        stack.push(i)
    result = ''
    for j in txt:
        result += stack.pop()
    print(result)

if __name__ == "__main__":

    print("Hello World! ")
    print("")
    string = "We will conquere COVID-19"
    print(revere_string_function(string))

