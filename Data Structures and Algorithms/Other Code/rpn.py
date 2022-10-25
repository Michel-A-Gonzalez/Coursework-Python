class Stack (object):

    def __init__ (self):

        self.stack = []

    def push (self, item):

        self.stack.append (item)

    def pop (self):

        return self.stack.pop()

    def peek (self):

        return self.stack[-1]

    def is_empty (self):

        return (len(self.stack) == 0)

    def size (self):

        return len(self.stack)

def operate (oper1, oper2, token):

    expr = str(oper1) + token + str(oper2)

    return eval(expr)

def rpn (s):

    operators = ['+', '-', '*', '/', '//', '%', '**']

    theStack = Stack()

    tokens = s.split()

    for item in tokens:

        if (item in operators):

            oper2 = theStack.pop()

            oper1 = theStack.pop()

            theStack.push (operate (oper1, oper2, item))

        else:

            theStack.push (float(item))

    return theStack.pop()

def main():

    in_file = open('rpn.txt', 'r')

    for line in in_file:

        line = line.strip()

        value = rpn (line)

        print(line, '=', value)

    in_file.close()

main()
