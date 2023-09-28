def minus(left, right):
    return left - right

def mult(left, right):
    return left * right

def div(left, right):
    if right != 0:
        return left / right
    else:
        return "Error: Dibagi oleh 0"

def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        if operator == '+':
            return tree(left) + tree(right)
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return expression

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:",result)
