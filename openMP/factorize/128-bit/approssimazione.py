# interpolazione tramite lagrange
def lagrange_interpolation(points, x):
    result = 0.0
    for i in range(len(points)):
        xi, yi = points[i][:2]
        term = yi
        for j in range(len(points)):
            if i != j:
                xj, yj = points[j][:2]
                term *= (x - xj) / (xi - xj)
        result += term
    return result

# Punti dati numero di bit, core hours presenti factorize.txt
points = [(32, 0.0078), (64, 0.31), (72, 1), (80, 7.9466)]

# Valore di x per cui si desidera calcolare la funzione approssimata
x = 128

# Calcolo del valore approssimato della funzione per x = 128
approximated_value = lagrange_interpolation(points, x)

print(f"Il valore approssimato della funzione per x = {x} è: {approximated_value}")
