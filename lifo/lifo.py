class LifoStack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.items.append(item)
        """Append item to the end of the stack."""

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

class Calculator:
    def __init__(self):
        self.stack = LifoStack()

    def evaluate(self, problem):
        for x in problem.split():
            if x.isdigit():
                self.stack.push(int(x))
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self._apply(x, operand1, operand2)
                self.stack.push(result)
        return self.stack.pop()

    def _apply(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            raise Exception(f"Unknown operator")
        
calc = Calculator()

try:

    problem1 = "3 4 +"
    result1 = calc.evaluate(problem1)
    print(f"Problem: {problem1}, Result: {result1}")  # 7

    problem2 = "10 5 -"
    result2 = calc.evaluate(problem2)
    print(f"Problem: {problem2}, Result: {result2}")  # 5

    problem3 = "2 3 *"
    result3 = calc.evaluate(problem3)
    print(f"Problem: {problem3}, Result: {result3}")  # 6

    problem4 = "8 2 /"
    result4 = calc.evaluate(problem4)
    print(f"Problem: {problem4}, Result: {result4}")  # 4.0

    problem5 = "3 4 + 2 * 7 /"
    result5 = calc.evaluate(problem5)
    print(f"Problem: {problem5}, Result: {result5}")  # 2.0

except Exception as e:
    print(f"Error: {e}")