def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
print(line_equation_of(point(6, -2), -2))
