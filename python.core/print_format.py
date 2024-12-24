def shades_01(n):
    return ["#{:02x}{:02x}{:02x}".format(v,v,v) for v in range(1,min(n+1, 255))]

print(shades_01(-10))


print([x for x in range(1, -10)])