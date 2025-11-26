# parametros posicionais com /
def func7(a, b, c, /, d="n/d", e="n/d", f="n/d"):
    return f"{a}, {b}, {c}, {d}, {e}, {f}"

print(func7(1, 2, 3))
print(func7(1, 2, 3, 4))
print(func7(1, 2, 3, d=4, e=5, f=6))

# parametros nomeados com *
def func8(a, b, *, c="n/d", d="n/d"):
    return f"{a}, {b}, {c}, {d}"

print(func8(1, 2))
print(func8(1, 2, c=3))
print(func8(1, 2, c=3, d=4))