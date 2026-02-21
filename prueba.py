import sympy as sp

# 1. Definir variables simbolicas
x, y = sp.symbols('x y')

# 2. Definir las funciones intermedias y la principal
u = x * y
v = x + y
f = sp.log(u**2 + v**2)

# 3. Calcular la derivada parcial respecto a x
df_dx = sp.diff(f, x)

print("--- Derivada Simbolica ---")
sp.pprint(df_dx)

# 4. Evaluar en el punto x=1, y=2 usando un diccionario
valor_evaluado = df_dx.subs({x: 1, y: 2})

print("\n--- Valor Numerico en (1, 2) ---")
print(f"Resultado exacto: {valor_evaluado}")
print(f"Resultado decimal: {valor_evaluado.evalf()}")