import sympy as sp

# Definir todas las variables simbolicas globales
x, y, z = sp.symbols('x y z')

print("\n" + "="*40)
print("   CÁLCULO MULTIVARIABLE CON SYMPY")
print("="*40)

print("\n--- Problema 1: Matriz Jacobiana ---")
# Definir y calcular
F = sp.Matrix([x**2 * y, sp.exp(x * y)])
J = F.jacobian([x, y])

# Evaluar
punto_jacobiana = {x: 1, y: 0}
J_evaluada = J.subs(punto_jacobiana)

# Imprimir resultados
print("Funcion vectorial F:")
sp.pprint(F)
print("\nMatriz Jacobiana analitica:")
sp.pprint(J)
print(f"\nMatriz Jacobiana evaluada en {punto_jacobiana}:")
sp.pprint(J_evaluada)


print("\n--- Problema 2: Matriz Hessiana ---")
# Definir y calcular
f = x**3 - 2*x*y**2 + y**3
variables_f = list(sp.ordered(f.free_symbols))
H = sp.hessian(f, variables_f)

# Evaluar
punto_hessiana = {x: 2, y: 1}
H_evaluada = H.subs(punto_hessiana)

# Imprimir resultados
print("Funcion f:")
sp.pprint(f)
print("\nMatriz Hessiana analitica:")
sp.pprint(H)
print(f"\nMatriz Hessiana evaluada en {punto_hessiana}:")
sp.pprint(H_evaluada)


print("\n--- Problema 3: Derivada Direccional ---")
# Definir y calcular
g = x**2 + y**2 + z**2
direccion = sp.Matrix([3, 0, 4]) / 5
grad_g = sp.Matrix([sp.diff(g, x), sp.diff(g, y), sp.diff(g, z)])
derivada_direccional = grad_g.dot(direccion)

# Evaluar
punto_direccional = {x: 1, y: -1, z: 2}
direccional_evaluada = derivada_direccional.subs(punto_direccional)

# Imprimir resultados
print("Funcion g:")
sp.pprint(g)
print(f"\nDerivada direccional en direccion {list(direccion)}:")
sp.pprint(derivada_direccional)
print(f"\nDerivada direccional evaluada en {punto_direccional}:")
sp.pprint(direccional_evaluada)
print("\n")