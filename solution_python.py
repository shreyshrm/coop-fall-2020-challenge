class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = []

    def add(self, num: int):
        self.value += num
        self.stack.append('add' + str(num))

    def subtract(self, num: int):
        self.value -= num
        self.stack.append('subtract' + str(num))

    def undo(self):
        if len(self.stack) == 0:
            return
        x = -1
        while self.stack[x] == 'undo':
            x -= 1 
        operation = self.stack[x]
        if operation[0:3] == "add":
            numberundo = operation[3:]
            numberundo = int(numberundo)
            self.value -= numberundo
            self.stack.append('undo')
        elif operation[0:8] == "subtract":
            numberundo = operation[8:]
            numberundo = int(numberundo)
            self.value += numberundo
            self.stack.append('undo')

    def redo(self):
        print(self.value)
        if len(self.stack) == 0:
            return
        x = -1
        operation = self.stack[x]
        while operation == 'undo':
            x -= 1
            operation = self.stack[x]
        else:
            return
        if operation[0:3] == "add":
            numberundo = operation[3:]
            numberundo = int(numberundo)
            self.value += numberundo
            self.stack.append('redo')
        elif operation[0:8] == "subtract":
            numberundo = operation[8:]
            numberundo = int(numberundo)
            self.value -= numberundo
        print(self.value)
        

    def bulk_undo(self, steps: int):
        stackLength = len(self.stack)
        for x in range(steps):
            if stackLength == 0:
                continue
            operation = self.stack[stackLength-1]
            if operation[0:3] == "add":
                numberundo = operation[3:]
                numberundo = int(numberundo)
                self.value -= numberundo
            elif operation[0:8] == "subtract":
                numberundo = operation[8:]
                numberundo = int(numberundo)
                self.value += numberundo
            stackLength -= 1

    def bulk_redo(self, steps: int):
        print(self.stack)
        numberUndos = 0
        for x in reversed(self.stack):
            if x == "undo":
                numberUndos += 1
                self.stack.pop()
        stepsToDo = numberUndos
        print('stepstodo: ',stepsToDo)
        for x in range(stepsToDo):
            operation = self.stack[-1]
            if operation[0:3] == "add":
                numberundo = operation[3:]
                numberundo = int(numberundo)
                self.value += numberundo
            elif operation[0:8] == "subtract":
                numberundo = operation[8:]
                numberundo = int(numberundo)
                self.value -= numberundo
