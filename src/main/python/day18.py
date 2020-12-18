def first_star(expressions): return calculate_sum_of_exrpressions(expressions, {'+' : 1, '*' : 1})
def second_star(expressions): return calculate_sum_of_exrpressions(expressions, {'+' : 2, '*' : 1})

def calculate_sum_of_exrpressions(expressions, precedence):
    tokens = [expression.replace("(", " ( ").replace(")", " ) ").split() for expression in expressions]
    return sum([calculate_rpn(infix_to_rpn(token, precedence)) for token in tokens])

def infix_to_rpn(tokens, precedence):
    is_operator = lambda token: token in precedence
    rpn_output = []
    stack = []
    
    for token in tokens:
        if is_operator(token):
            while stack and is_operator(stack[-1]):
                if precedence[token] <= precedence[stack[-1]]:
                    rpn_output.append(stack.pop())
                    continue
                break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                rpn_output.append(stack.pop())
            stack.pop()
        else:
            rpn_output.append(token)
    
    while len(stack) != 0:
        rpn_output.append(stack.pop())
    
    return rpn_output

def calculate_rpn(rpn_tokens):
    stack = []
    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y
        }

    for token in rpn_tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            first = stack.pop()
            second = stack.pop()
            result = operations[token](first, second)
            stack.append(result)
    
    return stack[0]


if __name__ == "__main__":
    math = open('src/main/resources/day18/input.txt', 'r').read().split("\n")
    print(first_star(math))
    print(second_star(math))