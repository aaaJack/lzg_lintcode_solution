class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, element):
        # write your code here
        self.stack1.append(element)
        
    def top(self):
        # write your code here
        # return the top element
        return self.stack1[0]
        
    def pop(self):
        # write your code here
        # pop and return the top element
        return self.stack1.pop(0)