def shades(n):
    if n <= 0: return [] 
    if n > 254: n = 254
    return ['#' + 3*('0' + hex(x)[2:]) if x < 16 else '#' + 3*hex(x)[2:] for x in range(1, n+1)]
print(shades(-10))


def shades_01(n):
    return ["#{:02x}{:02x}{:02x}".format(v,v,v) for v in range(1,min(n+1, 255))]

print(shades_01(10))