class Solution:
    def evaluate(self, tokens):
        myStack = []

        for token in tokens:
            if token in ["+","-","*","/"]:
                a = myStack.pop()
                b = myStack.pop()
                if token == "+":
                    c = a + b 
                elif token == "-":
                    c = b - a 
                elif token == "*":
                    c = a * b 
                else:
                    c = int(b/a)
                myStack.append(c)

            else:
                myStack.append(int(token))
        return myStack[-1]