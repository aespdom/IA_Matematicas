import sympy as sp

print("\n" + "="*40)
print("   ALGEBRA LINEAL: EIGEN Y DIAGONALIZACION")
print("="*40)

# Matriz del Problema 2 de hoy
A = sp.Matrix([
    [4, 1],
    [3, 2]
])

print("\nMatriz Original A:")
sp.pprint(A)

# 1. Extraer autovalores y autovectores
# .eigenvects() devuelve una lista de tuplas: (eigenvalue, multiplicidad, [eigenvectors])
eigen_info = A.eigenvects()

print("\n--- Autovalores y Autovectores ---")
for info in eigen_info:
    valor = info[0]
    vectores = info[2]
    print(f"\nPara lambda = {valor}:")
    sp.pprint(vectores[0])

# 2. Diagonalizar la matriz A = P * D * P^-1
# SymPy tiene un metodo directo que te devuelve P y D
P, D = A.diagonalize()

print("\n--- Diagonalizacion (A = P D P^-1) ---")
print("Matriz P (Autovectores en columnas):")
sp.pprint(P)

print("\nMatriz D (Autovalores en la diagonal):")
sp.pprint(D)

# Comprobacion matematica
print("\nComprobacion: ¿P * D * P^-1 es igual a A?")
comprobacion = P * D * P.inv()
sp.pprint(comprobacion)
print("\n")