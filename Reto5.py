productos = {
    "1": ["Tangelos", 9000, 67],
    "2": ["Limones", 2500, 35],
    "3": ["Peras", 2700, 65],
    "4": ["Arandanos", 9300, 34],
    "5": ["Tomates", 8100, 42],
    "6": ["Fresas", 9100, 90],
    "7": ["Helado", 4500, 41],
    "8": ["Galletas", 700, 18],
    "9": ["Chocolates", 4500, 80],
    "10": ["Jamon", 11000, 55]
}

ma = 0
mi = 1000000
mx = []
sp = 0
to = 0
res = True
acc = input()
c, n, p, i = input().split()


def agr(cod, nom, pro, inv):
    if cod in productos:
        resp = False
    else:
        productos.update({cod: [nom, pro, inv]})
        resp = True
    return resp


def act(cod, nom, pro, inv):
    if cod in productos:
        productos.update({cod: [nom, pro, inv]})
        resp = True
    else:
        resp = False
    return resp


def bor(cod):
    if cod in productos:
        productos.pop(cod)
        resp = True
    else:
        resp = False
    return resp


if acc == "AGREGAR":
    res = agr(c, n, p, i)
elif acc == "ACTUALIZAR":
    res = act(c, n, p, i)
elif acc == "BORRAR":
    res = bor(c)

if res:
    for x in productos:
        sp = sp + int(productos[x][1])
        to = to + (int(productos[x][1]) * int(productos[x][2]))
        pr = sp / len(productos)
        if int(productos[x][1]) > ma:
            ma = int(productos[x][1])
            cma = x
        if int(productos[x][1]) < mi:
            mi = int(productos[x][1])
            cmi = x
    print("{} {} {:.1f} {:.1f}".format(productos[cma][0], productos[cmi][0], pr, to))
else:
    print("ERROR")
