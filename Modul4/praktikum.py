import math

def translasi(tx, ty):
    return lambda x, y: (x + tx, y + ty)

def rotasi(sudut):
    return lambda x, y: (
        x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut)),
        x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut)),
    )

def dilatasi(sx, sy):
    return lambda x, y: (x * sx, y * sy)

def line_equation(x, y, M):
    C = y - M * x
    return f"y = {M:.2f}x + {C:.2f}"

def transformasi_decorator(trans_func, rot_func, scale_func):
    def decorator(func):
        def wrapper(x, y, M):
            trans_result = trans_func(x, y)
            rot_result = rot_func(*trans_result)
            scale_result = scale_func(*rot_result)
            return func(*scale_result, M)
        return wrapper
    return decorator

def main():
    x_input = float(input("Masukkan nilai x titik A: "))
    y_input = float(input("Masukkan nilai y titik A: "))
    gradien_awal = float(input("Masukkan gradien awal: "))
    tx_input = float(input("Masukkan nilai translasi tx: "))
    ty_input = float(input("Masukkan nilai translasi ty: "))
    sudut_rotasi = float(input("Masukkan sudut rotasi: "))
    sx_input = float(input("Masukkan perbesaran skala pada sumbu x: "))
    sy_input = float(input("Masukkan perbesaran skala pada sumbu y: "))

    trans = translasi(tx_input, ty_input)
    rot = rotasi(sudut_rotasi)
    dil = dilatasi(sx_input, sy_input)

    @transformasi_decorator(trans, rot, dil)
    def transformed_line_equation(x, y, M):
        return line_equation(x, y, M)

    result_equation = transformed_line_equation(x_input, y_input, gradien_awal)

    print(f"\nPersamaan garis yang melalui titik ({x_input},{y_input}) dan bergradien {gradien_awal:.2f}:")
    print(line_equation(x_input, y_input, gradien_awal))

    print("Persamaan garis setelah transformasi:")
    print(result_equation)

if __name__ == "__main__":
    main()
